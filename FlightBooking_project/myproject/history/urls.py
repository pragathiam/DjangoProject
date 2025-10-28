from django.urls import path
from history import views 
urlpatterns=[
    path('avability',views.avability),
    path('pendingtickets',views.pendingtickets)
    
]