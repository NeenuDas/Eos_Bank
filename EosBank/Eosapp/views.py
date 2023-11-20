from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('app_form')
        else:
            messages.info(request,"Invalid Login")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Exist")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Taken")
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
            return redirect('/')
    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def app_form(request):
    return render(request, "app_form.html")

def sucess(request):
    return render(request, 'success.html')

def home(request):
    return render(request, "home.html")

  # if request.method =="POST":
    #     username=request.POST['username']
    #     dob = request.POST['dob']
    #     phone = request.POST['phone']
    #     email = request.POST['email']
    #     address = request.POST['address']
    #     district = request.POST['district']
    #     branch = request.POST['branch']
    #     account_type = request.POST['account_type']
    #     materials_provided = request.POST['materials_provided']
    #     my_bank = Bank(username=username,dob=dob,phone=phone,email=email,address=address,district=district,branch=branch,account_type=account_type,materials_provided=materials_provided)
    #     my_bank.save()
    #     return redirect('/')
    # else: