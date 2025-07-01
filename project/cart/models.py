from django.db import models
from shop.models import *


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
    def _str_(self):
        return self.PRODUCT

