from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('mobiles',views.mobiles,name='mobiles'),
    path('laptops',views.laptops,name='laptops'),
]
    