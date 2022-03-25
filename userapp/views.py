from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout,authenticate
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def userlogin(request):
    if request.method=="POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')
        print(username, password)
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def userlogout(request):
    if request.user is logout:
        return redirect("/login")
    logout(request)
    return redirect("/login")