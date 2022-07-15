from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('stocks/', views.StockDataView.as_view()),
    path('create_user/', views.CreateUserView.as_view()),
    path('news/', views.GetNewsView.as_view()),
    path('add-stock/', views.StockDetailAddView.as_view()),
]
