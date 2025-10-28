from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add_product',views.add_product,name='add_product'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('remove',views.remove,name='remove')
]