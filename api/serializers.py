from django.contrib.auth import get_user_model
from rest_framework import serializers
from stocks.models import MyPortfolio, Excel_Upload

User = get_user_model()

class StockDataSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='User')
    class Meta:
        model = MyPortfolio
        fields = ("user", "stock_name", "stock_quantity", "is_favorite", "date", "purchased_price", )

class CreateUserSerislizer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'
        
        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user

class ExcelUploadSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='User')
    class Meta:
        model = Excel_Upload
        fields = ("user", "excel_upload", )