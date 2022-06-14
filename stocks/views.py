from django.contrib.auth import logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .news import  get_headlines
from .stock_search import get_stock_search
from django.contrib import messages

# Create your views here.

class IndexHomeView(View):
    template_name = 'index.html'
    headlines_get = get_headlines()
    headlines = headlines_get['articles'][0]
    headlines2 = headlines_get['articles'][1]
    def get(self, request):
        return render(request, self.template_name, {'headlines' : self.headlines,
                                                    'headlines2' : self.headlines2})


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

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request,'login.html')

def portfolio_page(request):
    return render(request, 'portfolio.html')

def get_stock_data(request):
    print(request.GET.get('search_value'))
    data = get_stock_search(request.GET.get('search_value'))
    
    return JsonResponse({'data': data})