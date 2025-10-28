from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete_/<int:pk>',views.delete_,name='delete_')
    
]
