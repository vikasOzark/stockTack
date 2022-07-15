from django.shortcuts import get_object_or_404, render
from requests import request
from rest_framework import generics
from stocks.news import get_headlines
from stocks.models import MyPortfolio
from . import serializers
from  rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
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