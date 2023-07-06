from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import User,profile,category
# Create your views here.

def home(request):
    
    cat = category.objects.all()
    
    data= {
        'cat':cat;
    }
    

    return render(request, "home.html")


def login(request):
    
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        user = auth.authenticate(username=uname, password=pwd)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/profile')
        else:
            return HttpResponse("uname , password invalid ")
        
    
    return render(request, "login.html")




def logout(request):
    auth.logout(request)

    return redirect('/')


def profile(request):
    
    if request.user.is_authenticated:
        
    
        return render(request, "profile.html")
    else:
        return redirect("/login")
    
    
def register(request):
    
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        
        
        # u = User(password=pwd, username=uname, email=email,first_name=fname, last_name=lname)
        
        User.objects.create_user(password=pwd, username=uname, email=email,first_name=fname, last_name=lname)
        
 
        return redirect('/profile')
    else:
        HttpResponse("faield")
    
    return render(request, "register.html")
    
