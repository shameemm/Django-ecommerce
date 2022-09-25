from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth
# from .models import Profile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            return redirect('home')
        else:
            return redirect('login')
    else:   
        return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email= request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Exists')
            return redirect('signup')
        else:
            print(password)
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email,phone=phone )
            # user=Profile.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email,phone=phone )
            user.save()
            print('success')
            return redirect(to='login')
    else:
        return render(request, 'signup.html')