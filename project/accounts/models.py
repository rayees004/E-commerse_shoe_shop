from django.db import models

# Create your models here.



class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.TextField(max_length=200)
    email = models.EmailField()
    password = models.TextField(max_length= 200)


class Address(models.Model):
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.TextField()
    pincode = models.IntegerField()
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    place = models.TextField()
    landmark = models.TextField()



