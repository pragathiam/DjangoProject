from django.shortcuts import render

# Create your views here.
def electronics_home(request):
    return render(request,'electronics_home.html')
def mobiles(request):
    return render(request,'mobiles.html')
def laptops(request):
    return render(request,'laptops.html')
def watches(request):
    return render(request,'watches.html')