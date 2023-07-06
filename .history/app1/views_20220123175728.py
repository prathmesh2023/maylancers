from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import User,profile

# Create your views here.

def home(request):

    return render(request, "home.html")


def login(request):
    
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        user = auth.authenticate(username=uname, password=pwd)
        
        
    
    return render(request, "login.html")
