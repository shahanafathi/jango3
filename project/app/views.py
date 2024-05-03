from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import CustomUser
from django.contrib.auth.models import auth
# from django.contrib.auth.models import User

# from django.contrib.auth.models import 

# Create your views here.

def index(request):
    return render(request,'index.html')

def abstr_reg(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        data=CustomUser.objects.create_user(first_name=name,age=age,email=email,phone=phone,username=username,password=password)
        data.save()
        return redirect(login)
    else:
        return render(request,'rgstr.html')
    

       
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    d = auth.authenticate(username=username,password=password)
    if d is not None:
      auth.login(request,d)
      return redirect(userhome)
    else:
      return HttpResponse('error')
  else:
    return render(request,'login.html')

def userhome(request):
    return render(request,'userhome.html')
 
def profile(request):
    a=CustomUser.objects.get(id=request.user.id)
    return render(request,'profile.html',{'aa':a})
    
def logout(request):
    auth.logout(request)
    return redirect(login)

def proedit(request):
    data = CustomUser.objects.get(id=request.user.id)
    if request.method=='POST':
        data.first_name=request.POST['name']
        data.age=request.POST['age']
        data.email=request.POST['email']
        data.phone=request.POST['phone']
        data.username=request.POST['username']
        data.password=request.POST['password']
        data.save()
        return redirect(profile)
    else:
        return render(request,'proedit.html',{'data1':data})
        