from django.shortcuts import render,redirect
from base.models import BookingDetails,BookingConfirmation

# Create your views here.
def home(request):
    data = BookingDetails.objects.all()
    return render(request, 'home.html', {'data': data})

def form_view(request):
    if request.method == 'POST':
        title_data = request.POST['title_attr']
        desc_data = request.POST['desc_attr']
        BookingDetails.objects.create(title=title_data, desc=desc_data)
        return redirect('home')
    return render(request, 'form.html')

def booking(request):
    return render(request, 'booking.html')


def update(request,pk):
    data=BookingDetails.objects.get(id=pk)
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
    data=BookingDetails.objects.get(id=pk)

    return render(request,'confirm_delete.html',{'record':data})

def delete_(request,pk):
    data=BookingDetails.objects.get(id=pk)
    BookingConfirmation.objects.create(title=data.title,desc=data.desc)
    data.delete()
    return redirect('home')

def history(request,pk):
    data=BookingDetails.objects.get(id=pk)
    
