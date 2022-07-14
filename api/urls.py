from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('all/', views.StockDataView.as_view()),
    path('create_user/', views.CreateUserView.as_view()),
    path('news/', views.GetNewsView.as_view()),
    path('add-stock/', views.StockDetailAddView.as_view()),
]
