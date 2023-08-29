from django.db import models

# Create your models here.
class User_info(models.Model):
    username =models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    passwrd = models.TextField(max_length=100)
