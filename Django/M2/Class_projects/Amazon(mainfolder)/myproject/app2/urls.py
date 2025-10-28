
from django.urls import path
from app2 import views as electronics
urlpatterns = [
    path('mobile/',electronics.mobile),
    path('laptop/',electronics.laptop),
    path('watches/',electronics.watches),
    path('tablets/',electronics.tablets),
    path('headphones',electronics.headphones)
]