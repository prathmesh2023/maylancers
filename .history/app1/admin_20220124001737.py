from django.contrib import admin
from django.contrib.auth.models import User
from .models import User,profile
from .models import category

# Register your models here.

admin.site.register(profile)

admin.site.register(category)