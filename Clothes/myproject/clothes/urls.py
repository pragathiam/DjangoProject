from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('shop/',views.shop),
    path('blog/',views.blog),
    path('pages/',views.pages),
    path('contact/',views.contact)
]    