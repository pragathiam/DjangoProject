from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  tomato(request):
    return HttpResponse("this is tomato")
def  apple(request):
    return HttpResponse("this is apple")
def  banana(request):
    return HttpResponse("this is banana")
def  orange(request):
    return HttpResponse("this is orange")
def  carrot(request):
    return HttpResponse("this is carrot")