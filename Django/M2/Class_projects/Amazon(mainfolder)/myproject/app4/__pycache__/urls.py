from django.urls import path
from app4 import views as fruits
urlspatterns=[
    path('tomato/',fruits.tomato),
    path('apple/',fruits.apple),
    path('banana/',fruits.banana),
    path('orange/',fruits.orange),
    path('carrot/', fruits.carrot)
]