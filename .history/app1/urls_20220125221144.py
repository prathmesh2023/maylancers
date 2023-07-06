from django.contrib import admin
from django.urls import path
from app1 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home , name="home"),
    path("login", views.login, name="login"),
    path("logout", views.logout,name="logout"),
    path("profile", views.profile, name="profile"),
    path("register", views.register, name="register"),
    path("post_job", views.post_job, name="post_job"),
    path("apply/<str:title>/<int:id>", views.apply, name="apply"),
    path("proposal", views.proposal, name="proposal"),
    path("category/<str:title>", views.category, name="category"),
    path("search", views.search,name="search"),
    path("categories", views.categories, name="categories"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
