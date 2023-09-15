from django.shortcuts import render, HttpResponse,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@login_required(login_url="loginpage")
def index(request):
    return render(request, 'song/main.html')
@login_required(login_url="loginpage")
def pictures(request):
    return render(request, 'song/pictures.html')

@login_required(login_url="loginpage")
def video(request):
    return render(request,'song/video.html')

def signup(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('loginpage')
    return render(request, 'song/signup.html')
def loginpage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, 'song/login.html')
def logoutPage(request):
    logout(request)
    return redirect('loginpage')