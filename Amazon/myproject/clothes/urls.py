from django.urls import path
from . import views

urlpatterns=[
    path('',views.clothes_home,name='clothes_home'),
    path('mens/',views.mens,name='mens'),
    path('womens/',views.womens,name='womens'),
    path('kids/',views.kids,name='kids')
    
]