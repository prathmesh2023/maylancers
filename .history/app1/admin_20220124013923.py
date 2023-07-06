from django.contrib import admin
from django.contrib.auth.models import User
from .models import User,profile
from .models import category,post

# Register your models here.

admin.site.register(profile)

admin.site.register(category)
admin.site.register(post)
