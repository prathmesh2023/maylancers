from django.contrib import admin
from django.contrib.auth.models import User
from .models import User,profile
from .models import category
from .models import post
from .models import proposal
from .models import rating

# Register your models here.

admin.site.register(profile)

admin.site.register(category)

admin.site.register(post)

admin.site.register(proposal)  

admin.site.register(rating)   
 

