from django.db import models
from django.contrib.auth.models import User
from .stock_search import previous_date
# Create your models here.

class MyPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=20)
    stock_quantity = models.PositiveIntegerField()
    is_favorite = models.BooleanField(default=False)    
    date = models.DateField(null=True)
    purchased_price = models.FloatField(null=True)


    def __str__(self):
        return self.stock_name
    
    @property
    def stock_price(self):
        try:
            stock_price = previous_date(self.stock_name)
            print(stock_price)
            stock_price = stock_price['close']

            return self.stock_quantity * stock_price
        except:
            return 'NOT_FOUND'

class Excel_Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    excel_upload = models.FileField(upload_to='media/')