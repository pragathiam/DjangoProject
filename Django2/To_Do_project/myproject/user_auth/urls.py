from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_,name='login_'),
    path('register',views.register,name='register'),
]