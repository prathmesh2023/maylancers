from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path("", views.home , name="home"),
    path("login", views.login, name="login"),
    path("profile", views.profile, name="profile")
]
