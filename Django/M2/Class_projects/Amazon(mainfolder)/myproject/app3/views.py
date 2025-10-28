from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def football(request):
    return HttpResponse("this is foot ball app3")
def badminton(request):
    return HttpResponse("this is badminton app3  ")
def chessboard(request):
    return HttpResponse("this is chessboard app3  ")
def throwball(request):
    return HttpResponse("this is throwball app3  ")
def shoes(request):
    return HttpResponse("this is shoes app3  ")




