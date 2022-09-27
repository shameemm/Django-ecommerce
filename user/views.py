from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# from .models import Profile

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        print('user=',user)
        return render(request,'home.html',{'user':user})
    else:
        return render(request,'home.html')


def login(request):
    if 'username' in request.session:
        print(request.session)
        return redirect(to='home')
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
            
        if user is not None and user.is_superuser==False:
            auth.login(request, user)
            request.session['username'] = username
            return redirect(to='home')
        else:
            # messages.info(request, 'Invalid credentials')
            return redirect(to='login')
        
            
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
            user.save()
            print('success')
            return redirect(to='login')
    else:
        return render(request, 'signup.html')  
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')