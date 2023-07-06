from cgitb import text
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import User,profile,category,post
from django.db.models import Q


# Create your views here.

def home(request):
    
    from .models import category,profile,post
    cat = category.objects.all().order_by('-id')
    
    from .models import post
    
    post = post.objects.all().order_by('-id')
    
    data= {
        'cat':cat,
        'post':post,
    }
    

    return render(request, "home.html", data)


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
    
    
def post_job(request):
    
    cat = category.objects.all().order_by('-id')
   

    data={
        "cat":cat,
    }
    
    if request.method == 'POST':
        wtitle = request.POST.get('wtitle')
        loc = request.POST.get('loc')
        desc = request.POST.get('desc')
        cat = request.POST.get('cat')
        thumb = request.FILES['file']
        afrom = request.POST.get('afrom')
        ato = request.POST.get('ato')
        username = request.POST.get('username')
        from .models import post
        
        job = post(title=wtitle, loc=loc, desc=desc, cat=cat, thumb=thumb, afrom=afrom, ato=ato,user=username)
        
        job.save()
            
        return redirect('/')
   
        
    return render(request, "postjob.html", data)



def apply(request, title, id):
    
    from .models import post
    
    post = post.objects.all().filter(title=title,id=id)[0]
    
    data = {
        'post':post,
    }
    
    
    return render(request, "apply.html",data)

def proposal(request):
    
    if request.method == 'POST':
        text = request.POST.get('text')
        username = request.POST.get('username')
        post_id = request.POST.get('post_id')
        mobile = request.POST.get('mobile')
        
        from .models import proposal,post
        
        p = proposal(text=text,user=username,post_id=post_id,mob=mobile)
        
        p.save()
        
    return HttpResponse("Sucees")


def category(request,title):
    
    from .models import post
    
    posts = post.objects.filter(cat=title).order_by('-id')
    title = title
    
    return render(request, "category.html", {'posts':posts ,'title':title })


def search(request):
    
    if request.method == 'POST':
        
        text = request.POST.get('text')
        
        from .models import post
        
        posts = post.objects.filter(Q(title=text) | Q(loc=text)).order_by('-id')
        
        data = {
            'posts':posts,
        }
    
        return render(request, "search.html", data)
    
    return HttpResponse("no query")