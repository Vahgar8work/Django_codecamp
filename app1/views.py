from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Service

def index(request):
    serv = Service.objects.all()
    return render(request , 'index.html', {'services':serv})

def inputy(request):
    return render(request , 'inputy.html')

def count(request):
    words = request.POST['text']
    size = len(words.split())
    return render(request,'Count.html',{"size":size , "text":words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['emailid']
        password = request.POST['pasword']
        password2 = request.POST['pasword2']
        
        if password != password2:
            messages.warning(request , "Please match the passwords and try again")
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request , "Email already exists")
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.info(request , "This username already exists, please choose a different one")
            return redirect('/register')
        else:
            User.objects.create_user(username=username , password=password , email=email)
            return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        identity = request.POST['username_email']
        pasword = request.POST['pasword']
        #user authentication
        user = auth.authenticate(username = identity , password = pasword)
        if user == None:
            user = auth.authenticate(email = identity , password = pasword)
        
        if user!= None:
            auth.login(request, user)
            return redirect('/')            # redirect to home
        else:
            messages.warning(request , 'Invalid Credentials')
            return redirect('/login')
    else:
        return render(request , 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect(request , '/')