from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime

from shop.models import *
from accounts.models import *


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id
class Item(models.Model):
    PRODUCT = models.ForeignKey(Product,on_delete=models.CASCADE)
    CART = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quntity = models.IntegerField()
    active = models.BooleanField(default=True)
    def _str_(self):
        return self.PRODUCT


