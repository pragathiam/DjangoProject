from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def businessclass(request):
    return HttpResponse('This is business')
def economic(request):
    return HttpResponse('This is economic')