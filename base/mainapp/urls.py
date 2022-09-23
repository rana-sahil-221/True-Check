from . import views
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse


urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home),
    path('customer/',views.customer,name='customer'),
    path('company/',views.company,name='company'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
]