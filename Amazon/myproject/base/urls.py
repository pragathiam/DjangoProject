from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('support/',views.support,name='support'),
    path('movies/',views.movies,name='movies'),
    path('clothes/',views.clothes,name='clothes'),
    path('electronics/',views.electronics,name='electronics')
]