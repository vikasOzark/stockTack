from django.contrib.auth import logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .news import  get_headlines
from .stock_search import  previous_date
from django.contrib import messages
from .models import MyPortfolio
import random
from .calculate import stock_value

# Create your views here.

class IndexHomeView(View):
    template_name = 'index_.html'

    def get(self, request):
        headlines_get = get_headlines()

        news_list = []
        data = stock_value(request)
        print(data)

        # randon_color = ['#'+''.join([random.choice('9876543210ABCDEF') for j in range(6)]) for i in range(10)]
        random_color = ['#39CCCC' ,'#0074D9' ,'#B10DC9' ,'#4169E1' ,'#6A5ACD' ,'#EE82EE']

        for news in range(len(headlines_get['articles'])):
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
    
    return render(request, template_name='portfolio.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request,'login.html')

def get_data(request):
    data = previous_date(request.GET.get('search_value'))
    print('in view : ',data)
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
    data = MyPortfolio.objects.filter(user=request.user)
    return render(request, 'data_view.html', {'data': data})