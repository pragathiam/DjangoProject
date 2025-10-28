from django.shortcuts import render,redirect
from .models import TaskModel

# Create your views here.
def home(request):
    #read
    #get
    a=TaskModel.objects.get(id=3)
    print(a.title) # TaskModel object(3) #django

    #all
    b=TaskModel.objects.all()
    print(b)
    for i in b:
        print(i.title)
    #water
    #java
    #django    

    #filter
    c=TaskModel.objects.filter(title='django')
    return render(request,'home.html',{'data':a,'all_data':b,'all_filter':c})

def home(request):

    if request.method == 'POST':
    #Create
    # a=TaskModel(title='python',desc='this is all about python')
    # a.save()
        TaskModel.objects.create(
            title=request.POST['title_attr'],
            desc=request.POST['desc_attr']
            )
    
    #read

    data=TaskModel.objects.all()

    return render(request,'home.html',{'data':data})

def update(request,pk):
    #old data
    task=TaskModel.objects.get(id=pk)
    #new
    if request.method == 'POST':
        title_new=request.POST['title_attr']
        desc_new=request.POST['desc_attr']
        print(title_new,desc_new)

        task.title=title_new
        task.desc=desc_new
        task.save()
        return redirect('home')

    return render(request,'update.html',{'task':task})

def delete_(request,pk):
    task=TaskModel.objects.get(id=pk)
    task.delete()
    return redirect('home')