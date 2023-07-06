from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=100)
    dp = models.ImageField('dp', upload_to="app1/img/dp")
    
    
class category(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    desc = models.text_field(max_length=1000)
   
