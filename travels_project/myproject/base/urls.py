from django.urls import path
from . import views
urlpatterns = [
    path('',views.Deals_and_offers,name='Deals_and_offers'),
    path('Destinations',views.Destinations,name='Destinations'),
    path('Holiday_package',views.Holiday_package,name='Holiday_package'),
    path('Hotels',views.Hotels,name='Hotels'),
    path('Support',views.Support,name='Support'),
    path('Read/<int:pk>/',views.read,name='read')
]