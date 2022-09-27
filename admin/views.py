from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
# def adminlogin(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user=auth.authenticate(username=username, password=password)
#         if user is not None and user.is_superuser==True:
#             return redirect('adminhome')
#     else:
#         return render(request, 'admin_login.html')
# def adminlogin(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user=auth.authenticate(username=username, password=password)
#         if user is not None and user.is_superuser==True:
#             return redirect('adminhome')
#     else:
#         return render(request, 'admin_login.html')
@login_required(login_url='adminlogin')
def adminhome(request):
    return render(request, 'admin_home.html')

def adminlogin(request):
    if 'uname' in request.session:
        return redirect(to='adminhome')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            auth.login(request, user)
            request.session['uname'] = username
            return redirect('adminhome')
            
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')
@login_required(login_url='adminlogin')
def users(request):
    users=User.objects.filter(is_superuser=False)
    
    return render(request, 'user_management.html',{'users':users})
@login_required(login_url='adminlogin')
def products(request):
    return render(request, 'product_management.html')
    
@login_required(login_url='adminlogin')
def category(request):
    return render(request, 'category_management.html')
@login_required(login_url='adminlogin')
def block(request):
    id=request.GET['id']
    user=User.objects.get(id=id)
    user.is_active=False
    user.save()
    return redirect('users')
@login_required(login_url='adminlogin')
def unblock(request):
    id=request.GET['id']
    user=User.objects.get(id=id)
    user.is_active=True
    user.save()
    return redirect('users')
@login_required(login_url='adminlogin')
def adminlogout(request):
    auth.logout(request)
    return redirect('adminlogin')
    

    