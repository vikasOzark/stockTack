from django.contrib.auth import get_user_model
from rest_framework import serializers
from stocks.models import MyPortfolio


User = get_user_model()

class StockDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyPortfolio
        fields = '__all__'