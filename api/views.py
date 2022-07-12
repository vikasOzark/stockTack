from urllib import response
from django.shortcuts import render
from requests import request
from rest_framework import generics

from stocks.models import MyPortfolio
from .serializers import StockDataSerializer
from  rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
# Create your views here.

class StockDataView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StockDataSerializer
    queryset = MyPortfolio.objects.all()


class AuthenticationView(APIView):
    def get(self, request, format=None):
        authentication_classes = [BasicAuthentication, SessionAuthentication]
        permission_classes = [IsAuthenticated]

        content = {
            'user': str(request.user),

            'auth': str(request.auth),
        }
        return response(content)