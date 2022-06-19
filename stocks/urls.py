from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexHomeView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('portfolio/portfolio-stock/', views.get_stock_data, name='portfolio-stock'),
    # path('get-data/', views.get_data, name='get-data'),
    path('data_view/', views.data_view, name='data_view'),
]

