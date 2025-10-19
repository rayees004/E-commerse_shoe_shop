from django.db import models

# Create your models here.
from django.urls import reverse

from accounts.models import Address



class Category(models.Model):
    class Meta:
        ordering=('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('cat_pr',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

class Product(models.Model):
    class Meta:
        ordering=('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return '{}'.format(self.name)
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    img = models.ImageField(upload_to='product',default='product.jpg')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField(default=False)
    price = models.IntegerField()
    CATEGORY = models.ForeignKey(Category,on_delete = models.CASCADE)#foreignkey
    def get_url(self):
        return reverse('details',args=[self.CATEGORY.slug,self.slug])




class Order_Summary(models.Model):
    ADDRESS = models.ForeignKey(Address,on_delete=models.CASCADE,default=None)
    PRODUCT = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    price = models.IntegerField(default=None)
    payment_type = models.BooleanField(default=True)

    def __str__(self):
        return self.PRODUCT.name





