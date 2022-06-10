from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MyPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=20)
    stock_quantity = models.PositiveIntegerField()
    is_favorite = models.BooleanField(default=False)
    