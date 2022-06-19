from django.db import models
from django.contrib.auth.models import User
from .stock_search import get_stock_search
# Create your models here.

class MyPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=20)
    stock_quantity = models.PositiveIntegerField()
    is_favorite = models.BooleanField(default=False)
    print('====> ')
    
    @property
    def stock_price(self):
        stock_price = get_stock_search(self.stock_name)
        # price = 

        # print('====> ', price)
        return self.stock_quantity * stock_price