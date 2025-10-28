
from django.urls import path
from app3 import views as sports
urlpatterns=[
    path('football',sports.football),
    path('badminton',sports.badminton),
    path('chessboard',sports.chessboard),
    path('throwball',sports.throwball),
    path('shoes',sports.shoes)]