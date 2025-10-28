from django.shortcuts import render,redirect
from base.models import Booking,Cancelling

# Create your views here.
def flight(request):
    data=Booking.objects.all()

    return render(request,'flight.html',{'data':data})
def status(request):
   # print(request.GET)
    # print(request.POST)
    
    if request.method == 'POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST=['desc_attr']
        print(title_data,desc_data)
        Booking.objects.create(title=title_data,desc=desc_data)
        return redirect('home')

    return render(request,'status.html')

def time(request):
    return render('This is time 8:30')

def destination(request):
    return render('This is destination')

def update(request,pk):
    data=Booking.objects.get(id=pk)

    if request.method == 'POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']

        data.title=title_data
        data.desc=desc_data
        data.save()
        return redirect('home')
        print(title_data,desc_data)
    

    return render(request,'update.html',{'data':data})

def confirm_delete(request,pk):
    data=Booking.objects.get(id=pk)

    return render(request,'confirm_delete.html',{'record':data})

def delete_(request,pk):
    data=Booking.objects.get(id=pk)
    Cancelling.objects.create(title=data.title,desc=data.desc)
    data.delete()
    return redirect('home')

def history(request,pk):
    data=Booking.objects.get(id=pk)
    

    

