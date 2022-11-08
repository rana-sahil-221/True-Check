from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from mainapp.models import Contact
from datetime import datetime
def home(request):
    return render(request,'mainapp/home.html')

def customer(request):
    return render(request,'mainapp/demo-custom.html')

def company(request):
    return render(request,'mainapp/company.html')

def contactus(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact =  Contact(email=email,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request,'Form has been submitted Successfully!')
    return render(request,'mainapp/contactus.html')
''''    
def contact(reqeust):
    if request.method == 'POST':
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact =  Contact(email=email,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request,'Form has been submitted Successfully!')
    return render(request,'mainappp/contactus.html')
'''
def signup(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        reg_user = User.objects.create_user(username,email,pass1)
        reg_user.save()
        messages.success(request, "Your account has been successfully created!!")
    return render(request,'mainapp/demo-custom.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username = username,password = pass1)

        if user is not None:
            login(request,user)
            uname = user.username
            return render(request,'mainapp/welcome.html',{'fname':uname})
        else:
            messages.error(request,'Wrong Credentials')
    return render(request,'mainapp/demo-custom.html')

def signout(request):
    logout(request)
    #messages.success(request,"Logged out successfully!!")
    return redirect('signup')


def company(request):
    return render(request,'mainapp/company.html')


