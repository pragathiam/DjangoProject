from django.urls import path
from app3 import views as fruits
urlpatterns=[
    path('tomato',fruits.tomato),
    path('apple',fruits.apple),
    path('bananna',fruits.bananna),
    path('orange',fruits.orange),
    path('carrot',fruits.carrot)
    ]