from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"authetication/index.html")

def signup(request):

    if request.method =="POST":

        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
    


        myuser.save()

        messages.success(request,"your account registered successfully.")

        return redirect('signin')



    return render(request,"authetication/signup.html")


def signin(request):
        

    if  request.method =="POST":
        
        username=request.POST['username']
        pass1=request.POST['pass1']
        
        user=authenticate(username=username,password=pass1)

        if user is not None: 
            login(request,user)
            fname=user.first_name
            return render(request,"authetication/index.html",{'fname':fname})
        else:
            messages.error(request,"bad credentials")
            return redirect('home')

    return render(request,"authetication/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')