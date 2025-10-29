from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def login_(request):
    return render(request,'login_.html')

def register(request):
    print(request.POST)
    
    if request.method == 'POST':
        first_name_data=request.POST['firstname']
        last_name_data=request.POST['lastname']
        username_data=request.POST['username']
        email_data=request.POST['email']
        password_data=request.POST['password']
        print(first_name_data,last_name_data,username_data,email_data,password_data)
        u=User.objects.create(
            first_name=first_name_data,
            last_name=last_name_data,
            username=username_data,
            email=email_data,
        )
        u.set_password(password_data)
        u.save()
        return redirect('login_')
        
    return render(request,'register.html')