from django.urls import path
from ticket import views
urlpatterns=[
    path('businessclass',views.businessclass),
    path('economic',views.economic),
    
]