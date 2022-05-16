from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method =='POST':
        user_name=request.POST['username']
        passw=request.POST['password']
        if User.objects.filter(username=user_name ).exists() and User.objects.filter(password=passw).exists():    
            messages.success(request," logined")
            return redirect('index')
        else:
            return redirect('register')

    else:   
        return render(request,'user_details/login.html')

def register(request):
    if request.method == 'POST':
        user_name=request.POST['username']
        if User.objects.filter(username=user_name).exists():
            messages.error(request," username undertaken")
            return redirect('register')
        else:
            passw=request.POST['password2']
            e_mail=request.POST['email']
            user=User.objects.create_user(username=user_name, password=passw, email=e_mail)
            user.save();
            auth.login(request,user)
            messages.success(request,"profile detail updated")
            return redirect('login')
    else:
        return render(request,'user_details/register.html')

def logout(request):
    return render(request,'user_details/logout.html')
