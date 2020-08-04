from django.db import models

# Create your models here.
class Signup(models.Model):
    fn=models.CharField(max_length=100)
    ln=models.CharField(max_length=100)
    dob=models.DateField
    em=models.EmailField
    pw=models.CharField(max_length=20)
    cp=models.CharField(max_length=20)
    loc=models.TextField(max_length=100)
class Login(models.Model):
    ce=models.EmailField
    pc=models.CharField(max_length=20)

