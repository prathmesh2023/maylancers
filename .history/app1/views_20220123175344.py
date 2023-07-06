from django.shortcuts import render
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):

    return render(request, "home.html")


def login(request):
    
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        
    
    return render(request, "login.html")
