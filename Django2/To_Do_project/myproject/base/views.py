from django.shortcuts import render,redirect
from base.models import TaskModel
from django.db.models import Q

# Create your views here.
def home(request):

    all_data=TaskModel.objects.filter(host=request.user)

    if 'q' in request.GET:
        q=request.GET['q']
        all_data=TaskModel.objects.filter(Q(title__icontains=q) & Q(host=request.user)| Q(desc__icontains=q) & Q(host=request.user))
    else:
        all_data=TaskModel.objects.filter(host=request.user)    

    return render(request,'home.html',{'data':all_data})

def add(request):

    if request.method == 'POST':
        title_data=request.POST['title_data']
        desc_data=request.POST['desc_data']
        TaskModel.objects.create(
            title=title_data,
            desc=desc_data,
            host=request.User
        )
        return redirect('home')
    return render(request,'add.html')

def update(request,pk):
    #old data
    task=TaskModel.objects.grt(id=pk)

    #new data
    if request.method == 'POST':
        title_data=request.POST['title_data']
        desc_data=request.POST['desc_data']

        task.title=title_data
        task.desc=desc_data
        task.save()
        return redirect('home')
    return render(request,'update.html',{'task':task})

def delete(request,pk):
    task=TaskModel.objects.get(id=pk)
    task.delete()
    return redirect('home')