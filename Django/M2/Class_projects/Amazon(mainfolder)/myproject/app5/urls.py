from django.urls import path
from app5 import views as cosmetics
urlpatterns=[
    path('lipstic/',cosmetics.lipstick),
    path('foundation/',cosmetics.foundation),
    path('primer',cosmetics.primer),
    path('blush/',cosmetics.blush),
    path('kajal/',cosmetics.kajal)
    ]

