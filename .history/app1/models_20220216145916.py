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
    thumbnail = models.ImageField('thumbnail', upload_to="app1/img/category")
    desc = models.TextField()
    
    
    def __str__(self):
        return self.title
    

class post(models.Model):
    
    title = models.CharField(max_length=200)
    loc = models.CharField(max_length=200)
    desc = models.TextField()
    cat = models.CharField(max_length=200)
    thumb = models.ImageField('thumb', upload_to="app1/img/post/thumb")
    afrom = models.IntegerField()
    ato = models.IntegerField()
    user = models.CharField(max_length=200,default="def")
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
class proposal(models.Model):
    
    post = models.ForeignKey("post",  on_delete=models.CASCADE ,default=1)
   
    text = models.TextField()
    
    mob = models.CharField(max_length=150)
    
    user = models.CharField(max_length=150)
   
   
       
    def __str__(self):
        return self.user
    
    
class rating(models.Model):
    user = models.CharField(max_length=500)
    msg = models.CharField(max_length=1000)
