from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, "home.html")


def login(request):
    
    if post.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        
        print(uname, pwd)
    
    return render(request, "login.html")
