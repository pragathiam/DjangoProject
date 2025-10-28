from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contactus(request):
    return HttpResponse('This is contactus 987654321')
def mail(request):
    return HttpResponse('This is mail')
