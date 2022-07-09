from os import execl
from django.contrib.auth import logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.views import View
from .news import get_headlines
from .stock_search import  previous_date
from django.contrib import messages
from .models import MyPortfolio, Excel_Upload
import random
from .calculate import stock_value
from .serializers import StockSerializer
import pandas as pd
from django.http import JsonResponse
import random
from .forms import FeedBack
from .tasks import attachment_send_task

# Create your views here.

class IndexHomeView(View):
    template_name = 'index_.html'

    def get(self, request):

        data = stock_value(request)

        # randon_color = ['#'+''.join([random.choice('9876543210ABCDEF') for j in range(6)]) for i in range(10)]
        random_color = ['c-border-1', 'c-border-2', 'c-border-3', 'c-border-4', 'c-border-5', 'c-border-6', 'c-border-7', 'c-border-8', 'c-border-9', 'c-border-10']

        headlines_get = get_headlines()
        news_list = []
        for news in range(len(headlines_get['articles'])):
            img = headlines_get['articles'][news]['urlToImage']
            content = headlines_get['articles'][news]['content']
            if img and content is not None:
                print(news)
                news_list.append(headlines_get['articles'][news])

        context = {
            'news_list' : news_list,
            'random_color':random_color,
            'stock_data':data
            }

        return render(request, self.template_name, context=context )
    
def register(request):
    method = request.method

    if method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if request.POST is not None:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')

            elif password != password2:
                messages.error(request, 'Passwords do not match')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, 
                    password=password, 
                    email=email, 
                    first_name=first_name, 
                    last_name=last_name
                )

                user.save()

    return render(request, template_name='register.html')


def login(request):
    method = request.method

    if method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    
    return render(request, template_name='login.html')

def logout_user(request):
    if request.method == "POST":
        logout(request)
    return render(request,'login.html')

def get_data(request):
    data = previous_date(request.GET.get('search_value'))
    return JsonResponse({'data': data})

def data_saving(request):
    # data = previous_date(request.GET.get('search_value'))
    if request.method == 'POST': 
        stock_name = request.POST.get('stock_name')
        stock_date = request.POST.get('stock_date')
        stock_quantity = request.POST.get('stock_quantity')
        purchase_price = request.POST.get('stock_price')

        # sving the data to the database
        if stock_date == '':
            messages.info(request, 'Please enter a date')
            return render(request, 'portfolio.html')
        else:
            portfolio_model = MyPortfolio(
                user=request.user, 
                stock_name=stock_name,
                stock_quantity=stock_quantity,
                date = stock_date,
                purchased_price = purchase_price
            )

            portfolio_model.save()
        return JsonResponse({'success': 'data saved',
                             'status':200
                                })

def data_view(request):
    if request.user is not None:
        data_all = MyPortfolio.objects.filter(user=request.user)
        data = MyPortfolio.objects.filter(user=request.user).values('stock_name').distinct()    # getting the distinct stock names
        excel_files = Excel_Upload.objects.filter(user=request.user).order_by('-id')
        random_color = ['c-border-1', 'c-border-2', 'c-border-3', 'c-border-4', 'c-border-5', 'c-border-6', 'c-border-7', 'c-border-8', 'c-border-9', 'c-border-10']
        card_bg = ['stock-f-card-1', 'stock-f-card-2', 'stock-f-card-3', 'stock-f-card-4', 'stock-f-card-5']
    else:
        data = None
    return render(request, 'data_view.html', {'data': data, 'excel_files':excel_files, 'random_color':random_color, 'card_bg':card_bg, 'data_all':data_all})

class ExportImport(View):
    def get(self, request):
        stock_object = MyPortfolio.objects.filter(user=request.user)
        serializer = StockSerializer(stock_object, many=True,)
        df = pd.DataFrame(serializer.data)
        file_path = f'excel-file/stock-data{random.randint(1,10)}.xlsx'
        excel_file = df.to_excel(
            file_path,
            encoding='UTF-8', 
            index=False
            )
        excel_model = Excel_Upload(excel_upload=file_path, user=request.user)
        excel_model.save()
        return JsonResponse(df.to_json(), safe=False)

    def post(self, request):

        file = request.FILES.get('file')
        if file is not None:

            df = pd.read_excel(file)
            sheet_values = df.values.tolist()
            for index in range(len(sheet_values)):
                stock_model = MyPortfolio(
                    user=request.user, 
                    stock_name=sheet_values[index][1],
                    stock_quantity=sheet_values[index][2],
                    date = sheet_values[index][4],
                    purchased_price = sheet_values[index][5]
                )
                stock_model.save()
                print('n data saved')
            else:
                messages.info(request, 'Please choose a excel file first !')
                print('Please choose a excel file first !')
                return render(request, 'index_.html')

        return render(request, 'index_.html')

class FeedbackEmailView(FormView):
    template_name = 'feedback.html'
    form_class = FeedBack
    success_url = '/'

    def form_valid(self, form):
        print('enterd in form validaton')
        form.send_email()
        msg = 'thnks for your feedback'
        return HttpResponse(msg)

def attachment_send(request):
    method = request.method 
    if method == 'GET':
        file_id = request.GET.get('id')
        file_name = Excel_Upload.objects.get(id=file_id)
        attachment_send_task(request, file_name.excel_upload)
    return JsonResponse({'Data' : 'Got the id .'})
def excel_delete(request):
    method = request.method
    if method == 'GET':
        file_id = request.GET.get('id')
        file_name = Excel_Upload.objects.get(id=file_id)
        file_name.delete()
        return JsonResponse({'status': 200})