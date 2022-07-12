from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('all/', views.StockDataView.as_view()),
    path('auth/', obtain_auth_token)
]
