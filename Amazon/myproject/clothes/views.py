from django.shortcuts import render

# Create your views here.
def mens(request):
    return render(request,'mens.html')
def womens(request):
    return render(request,'womens.html')
def kids(request):
    return render(request,'kids.html')
def clothes_home(request):
    return render(request,'clothes_home.html')
