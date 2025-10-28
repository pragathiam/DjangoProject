from django.shortcuts import redirect,render
from django.contrib.auth.models import user
from django.contrib.auth import authenticate

# Create your views here.
def login_(request):
    if request.method == 'POST':
        username_data=request.POST['username']
        pass_data=request.POST['password']
        u=authenticate(Username=username_data,password=pass_data)
        print(u) # None # sri
        if u: 
            return redirect('home')   
        
    return render(request,'login_.html')    

def register(request):
    if request.method == 'POST':
        First_name_data=request.POST['Firstname']
        Last_name_data=request.POST['Lastname']
        User_name_data=request.POST['Username']
        email_data=request.POST['email']
        password_data=request.POST['password']
        print(First_name_data,Last_name_data,User_name_data,email_data,password_data)
        u=user.objects.create(
            first_name=First_name_data,
            last_name=Last_name_data,
            email=email_data,
            username=User_name_data,
        )
        u.set_password(password_data)
        u.save()
        return redirect('login')
    return render(request,'register.html')
