from urllib import response
from django.shortcuts import render
from requests import request
from rest_framework import generics

from stocks.models import MyPortfolio
from .serializers import StockDataSerializer
from  rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
# Create your views here.

class StockDataView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StockDataSerializer
    queryset = MyPortfolio.objects.filter(user = request.user)


class AuthenticationView(APIView):
    def get(self, request, format=None):
        authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
        permission_classes = [IsAuthenticated]

        content = {
            'user': str(request.user),

            'auth': str(request.auth),
        }
        return response(content)