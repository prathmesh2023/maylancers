from django.db import models

# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=100)
    dp = models.ImageField('dp', upload_to="mob1/images/user/profile/dp")
   
