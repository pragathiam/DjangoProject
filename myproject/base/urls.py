from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('news', views.news,name='news'),
    path('events', views.events,name='events'),
    path('about', views.about,name='about'),
    path('read/<int:pk>/', views.read,name='read'),
    path('readmore/<int:pk>/', views.readmore,name='readmore'),
    ]
   
