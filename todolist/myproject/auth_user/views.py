from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_(request):
    if request.method=="POST":
        username_data=request.POST['username']
        password_data=request.POST['password']
        u=authenticate(username=username_data,password=password_data)
        if u:
            login(request,u)
            return redirect('home')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        first_name_data=request.POST['first_name']
        last_name_data=request.POST['last_name']
        email_data=request.POST['email']
        username_data=request.POST['username']
        password_data=request.POST['password']
        try:
            u=User.objects.get(username=username_data)
            return render(request,'register.html',{'Status':True})
        except:
            u=User.objects.create(
                first_name=first_name_data,
                last_name=last_name_data,
                email=email_data,
                username=username_data,
                # password=pass_data
            )
            u.set_password(password_data)
            u.save()
            return redirect('login_')
        

    return render(request,'register.html')
@login_required(login_url='login_')
def profile(request):
    data=User.objects.all()
    return render(request,'profile.html',{'data':data})
def logout_(request):
    logout(request)
    return redirect('login_')
def change_password(request):

    if request.method == 'POST':
        try:
            u=User.objects.get(username=request.user.username)
            old_pass_data=request.POST['oldpassword']
            old_pass_verified=authenticate(username=u.username,password=old_pass_data)
            if old_pass_verified:
                print('old pass is matching')
                return render(request,'change_password.html',{'oldpassword_match':True})
            else:
                return render(request,'change_password.html',{'oldpassword_notmatch':True})
        except:
                new_pass_data=request.POST['newpassword']
                u.set_password(new_pass_data)
                u.save()
                return redirect('login_')
    return render(request,'change_password.html')

def Update_User_details(request,pk):
     data=User.objects.get(id=pk)
     if request.method=='POST':
        firstname_data=request.POST['first_name']
        lastname_data=request.POST['last_name']
        email_data=request.POST['email']
        username_data=request.POST['username']
        data.first_name=firstname_data
        data.last_name=lastname_data
        data.email=email_data
        data.username=username_data
        data.save()
        return redirect('profile')
     return render(request,'update_det.html',{'data':data})
