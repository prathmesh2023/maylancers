from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, "base.html")


def login(request):
    
    return render(request, "login.html")
