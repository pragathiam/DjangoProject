from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('update/<int:pk>',views.update,name='update'),
    path('update_/<int:dk>',views.delete_,name='delete_')
]

