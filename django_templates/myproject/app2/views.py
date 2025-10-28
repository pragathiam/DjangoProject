from django.shortcuts import render,HttpResponse

# Create your views here.
def mobile(request):
    return render(request,'all_html_app2/mobile.html')

def laptop(request):
    return render(request,'all_html_app2/laptop.html')

def watch(request):
    return render(request,'all_html_app2/watch.html')
