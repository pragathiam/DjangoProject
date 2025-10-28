from django.urls import path
from support import views
urlpatterns=[
    path('contactus',views.contactus),
    path('mail',views.mail),
    
]