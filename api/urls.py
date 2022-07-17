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

    path('stocks/', views.StockDataView.as_view()), # all stocks saved data by the user according tp the user type
    path('create/', views.CreateUserView.as_view()), # create a new user with basic permission
    path('news/', views.GetNewsView.as_view()), # get news from the news api
    path('add-stock/', views.StockDetailAddView.as_view()), # add a new stock to the user's portfolio
    path('stock-value/', views.StockValueDataView.as_view()), # get the stock value of the user's portfolio {P&L}
    path('excel-save/', views.StockDataExcelView.as_view()), # save the stock data to excel file | GET = save your data in excel file, POST= upload your data from excel file
    path('excel-format/', views.ExcelFormatView.as_view()), # get the excel format of the stock data
]

