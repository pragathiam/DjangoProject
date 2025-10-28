from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lipstick(request):
    return HttpResponse("lipstict")
def foundation(request):
    return HttpResponse("foundation")
def primer(request):
    return HttpResponse("primer")
def blush(request):
    return HttpResponse("blush")
def kajal(request):
    return HttpResponse("kajal")



