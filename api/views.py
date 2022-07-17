from django.http import JsonResponse
from rest_framework import generics
from yaml import serialize
from stocks.news import get_headlines
from stocks.models import MyPortfolio
from . import serializers
from  rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from stocks.calculate import stock_value
from stocks.views import ExportImport, download_excel

# Create your views here.

class StockDataView(generics.ListAPIView):
    
    authentication_classes = [JWTAuthentication, SessionAuthentication,]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.StockDataSerializer
    
    def get_queryset(self):
        user = self.request.user
        print('user :', user)
        try :
            if user.is_superuser:
                print('in admin', IsAdminUser)
                return MyPortfolio.objects.all()
            else:
                print('in none admin :')
                return MyPortfolio.objects.all().filter(user=user)
        except:
            return None

class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.CreateUserSerislizer
    permission_classes = [permissions.BasePermission]


class GetNewsView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        return Response(get_headlines())

class StockDetailAddView(generics.CreateAPIView):
    serializer_class = serializers.StockDataSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, ]
    permission_classes = [IsAuthenticated ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class StockValueDataView(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        stock_value_data = stock_value(request)
        return Response(stock_value_data)

class StockDataExcelView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    serializer_class = serializers.ExcelUploadSerializer

    def get(self, request):
        ExportImport.get(self, request)
        return JsonResponse({'message':'success'
                                'data'})

    def post(self, request):
        ExportImport.post(self, request)
        return JsonResponse({'message':'success'})
    
class ExcelFormatView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    def get(self, request):
        return download_excel(request)
