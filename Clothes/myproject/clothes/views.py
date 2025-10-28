from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'all_html/home.html')
def shop(request):
    return render(request,'all_html/shop.html')
def blog(request):
    return render(request,'all_html/blog.html')
def pages(request):
    return render(request,'all_html/pages.html')
def contact(request):
    return render(request,'all_html/contact.html')