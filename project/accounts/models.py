from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.TextField(max_length=200)
    email = models.EmailField()
    password = models.TextField(max_length= 200)
