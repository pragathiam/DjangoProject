from django.shortcuts import render,redirect
from base.models import ArtilceModel,HistoryModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@login_required(login_url='login_')
def home(request):
    if request.user.is_authenticated:
     if 'q' in request.GET:
        q=request.GET['q']
        data=ArtilceModel.objects.filter(Q(title__icontains=q) & Q(host=request.user) |Q(desc__icontains=q) & Q(host=request.user))
     else:
        data=ArtilceModel.objects.filter(host=request.user)
     return render (request,'home.html',{'data':data})

@login_required(login_url='login_')
def add(request):
    if request.user.is_authenticated:
     if request.method=='POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']
        data=ArtilceModel.objects.create(title=title_data,desc=desc_data,host=request.user)
        return redirect('home')
    return render(request,'add.html')

@login_required(login_url='login_')
def update(request,pk):
   if request.user.is_authenticated:
    data=ArtilceModel.objects.get(id=pk)
    if request.method=='POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']
        data.title=title_data
        data.desc=desc_data
        data.save()
        return redirect(home)
   return render(request,'update.html',{'data':data})

@login_required(login_url='login_')
def confirm_delete(request,pk):
    if request.user.is_authenticated:
     data=ArtilceModel.objects.get(id=pk)
    return render (request,'confirmdelete.html',{'data':data})

@login_required(login_url='login_')
def deleted_(request,pk):
    if request.user.is_authenticated:
     data=ArtilceModel.objects.get(id=pk)
     HistoryModel.objects.create(title=data.title,desc=data.desc,host=request.user)
     data.delete()
    return redirect('home')

@login_required(login_url='login_')
def history(request):
    if request.user.is_authenticated:
     data=HistoryModel.objects.filter(host=request.user)
    return render(request,'history.html',{'data':data})
    
@login_required(login_url='login_')
def restore(request, pk):
    if request.user.is_authenticated:
     data = HistoryModel.objects.get(id=pk)
     ArtilceModel.objects.create(
        title=data.title,
        desc=data.desc,
        host=request.user
    )
     data.delete()
    return redirect('history')

@login_required(login_url='login_')
def delete_all_history(request):
    if request.user.is_authenticated:
     HistoryModel.objects.all().delete()
    return redirect('history')

@login_required(login_url='login_')
def delete_history(request,pk):
    if request.user.is_authenticated:
     data=HistoryModel.objects.get(id=pk)
     data.delete()
    return redirect('history')

@login_required(login_url='login_')
def restore_all(request):
    if request.user.is_authenticated:
     data = HistoryModel.objects.all()
     for item in data:
        ArtilceModel.objects.create(
            title=item.title,
            desc=item.desc
        )
        item.delete()
    return redirect('history')

