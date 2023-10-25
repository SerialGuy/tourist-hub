from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("blogs",views.blogs,name='blogs'),
    path("signup",views.signup,name='signup'),
    path("signin",views.signin,name = 'signin'),
    path("signout",views.signout ,name = 'signout'),
    path("createuser",views.createuser, name = 'createuser'),
    path("loginuser",views.loginuser, name = 'loginuser'),
    path("mohadi-info",views.mohadi,name = "info")
]