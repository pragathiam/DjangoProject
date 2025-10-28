from django.urls import path
from . import views

urlpatterns=[
    path('mobile/',views.mobile),
    path('laptop/',views.laptop),
    path('watch/',views.watch)
]