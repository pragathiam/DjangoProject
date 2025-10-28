from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def support(request):
    return render(request,'support.html')
def movies(request):
    return render(request,'movies.html')
def clothes(request):
    return render(request,'clothes.html')
def electronics(request):
    return render(request,'electronics.html')