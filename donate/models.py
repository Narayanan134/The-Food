from django.db import models

# Create your models here.

class youdonate(models.Model):
    ydname=models.CharField(max_length=100)
    ydaddress=models.CharField(max_length=1000)
    yddaddress=models.CharField(max_length=1000)
    ydcontact=models.IntegerField(max_length=20)
    ydpeople=models.IntegerField(max_length=2000)
    ydfood=models.CharField(max_length=1000)

class donatethe(models.Model):
    tdname=models.CharField(max_length=100)
    tdaddress=models.CharField(max_length=1000)
    tdcontact=models.IntegerField(max_length=20)
    tdpeople=models.IntegerField(max_length=2000)
    tdorphanage=models.CharField(max_length=100)