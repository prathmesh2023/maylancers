from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, "home.html")


def login(request):
    
    if post.method == 'POST':
        uname = request.post.get('uname')
        pwd = request.post.get('pwd')
        
        print(uname)
    
    return render(request, "login.html")
