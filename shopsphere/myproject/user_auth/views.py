from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import logout

# Create your views here.
def login_(request):
    #wrong credentials
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if u:
            login(request,u)
            return redirect('home')
    return render(request,'login_.html')    

def register(request):  
    #intregity
    #password length   
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        u=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            username=username,
        )
    return render(request,'register.html')

def profile(request):

    return render(request,'profile.html')

def logout_(request):
    logout(request)
    return redirect('login_')    



        
