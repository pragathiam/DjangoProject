from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'all_html/home.html')

def about(request):
    return render(request,'all_html/about.html')

def support(request):
    return render(request,'all_html/support.html')
