from django.db import models

# Create your models here.
from django.urls import reverse

from accounts.models import User


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
