from django.db import models

# Create your models here.

class breakfastt(models.Model):
    qtyi=models.IntegerField()
    qtyd=models.IntegerField()
    qtypon=models.IntegerField()
    qtyth=models.IntegerField()
    qtyup=models.IntegerField()
    qtypoo=models.IntegerField()
class lunchh(models.Model):
    qtycurd=models.IntegerField()
    qtydal=models.IntegerField()
    qtylem=models.IntegerField()
    qtytam=models.IntegerField()
    qtyvr=models.IntegerField()
class dinnerr(models.Model):
    qtyi=models.IntegerField()
    qtyd=models.IntegerField()
    qtypon=models.IntegerField()
    qtyth=models.IntegerField()
    qtyup=models.IntegerField()
    qtypoo=models.IntegerField()

class img1(models.Model):
    idliimg=models.ImageField(upload_to='pics')
    dosaimg=models.ImageField(upload_to='pics')
    pongimg=models.ImageField(upload_to='pics')
    uthimg=models.ImageField(upload_to='pics')
    upmaimg=models.ImageField(upload_to='pics')
    pooriimg=models.ImageField(upload_to='pics')

class img2(models.Model):
    curdimg=models.ImageField(upload_to='pics')
    dalimg=models.ImageField(upload_to='pics')
    lemimg=models.ImageField(upload_to='pics')
    tamimg=models.ImageField(upload_to='pics')
    vrimg=models.ImageField(upload_to='pics')

class img3(models.Model):
    idliimg=models.ImageField(upload_to='pics')
    dosaimg=models.ImageField(upload_to='pics')
    pongimg=models.ImageField(upload_to='pics')
    uthimg=models.ImageField(upload_to='pics')
    upmaimg=models.ImageField(upload_to='pics')
    pooriimg=models.ImageField(upload_to='pics')

class details(models.Model):
    nameofc=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    contact=models.IntegerField()