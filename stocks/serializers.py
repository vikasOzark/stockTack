from rest_framework import serializers
from .models import MyPortfolio

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPortfolio
        fields = '__all__'
        
        read_only_fields = ('user',)
        extra_kwargs = {
            'user': {'read_only': True},
        }