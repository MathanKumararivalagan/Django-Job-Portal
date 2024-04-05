from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Portal.models import *
from django.contrib.auth import login as authlogin

from Portal.email import *

def home(request):
    return render(request,'Home/home.html')


#user login

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Emailbackend.authenticate(request,
                                     username=email,
                                     password=password)
        
        if user is not None:
           authlogin(request,user)
           return render(request,"userhome.html")
       
        else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
    
    return render(request,"Signup/login.html")
       


def Register(request):
    if request.method=="POST":
        username= request.POST.get('username')
        email= request.POST.get('email')
        password=request.POST.get('password')


        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')
        
    return render(request,"Signup/register.html")




# Recruiter login

def Reclogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Emailbackend.authenticate(request,
                                     username=email,
                                     password=password)
        
        if user is not None:
           authlogin(request,user)
           return render(request,"rechome.html")
        else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
    
    return render(request,"Rec_Signup/rec-login.html")
       


def RecRegister(request):
    if request.method=="POST":
        username= request.POST.get('username')
        email= request.POST.get('email')
        password=request.POST.get('password')


        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('rec-login')
        
    return render(request,"Rec_Signup/rec-register.html")
