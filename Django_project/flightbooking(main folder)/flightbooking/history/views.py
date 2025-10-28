from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def avability(request):
    return HttpResponse('This is avability')
def pendingtickets(request):
    return HttpResponse('This is pendingtickets')
