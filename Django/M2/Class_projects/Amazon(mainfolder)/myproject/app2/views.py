from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mobile(request):
    return HttpResponse("this is mobile view app2")
def laptop(request):
    return HttpResponse("this is laptop view app2")
def watches(request):
    return HttpResponse("this is watches view app2")
def tablets(request):
    return HttpResponse("this is tablets view app2")
def headphones(request):
    return HttpResponse("this is headphones view app2")