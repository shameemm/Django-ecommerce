from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('users',views.users,name='users'),
    path('products',views.products,name='products'),
    path('category',views.category,name='category'),
    path('block',views.block,name='block'),
    path('unblock',views.unblock,name='unblock'),

]
