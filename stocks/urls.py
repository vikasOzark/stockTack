from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexHomeView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]

