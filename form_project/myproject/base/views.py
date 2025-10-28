from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentModel

# Create your views here.
def home(request):

    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context={
        'form':StudentForm(),'data':StudentModel.objects.all()
    }
    return render(request,'home.html',context)

def update(request,pk):
    stu=StudentModel.objects.get(id=pk)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=stu)
        if form.is_valid():
            form.save()
    context={
        'form':StudentForm(instance=stu)
    }
    return render(request,'update.html',context)

def delete_(request,dk):
    task=StudentModel.objects.get(id=dk)
    task.delete_()
    return redirect('home')