from django.urls import path
from . import views

urlpatterns=[
    path('',views.electronics_home,name='electronics_home'),
    path('mobiles/',views.mobiles,name='mobiles'),
    path('laptops/',views.laptops,name='laptops'),
    path('watches/',views.watches,name='watches')
]
