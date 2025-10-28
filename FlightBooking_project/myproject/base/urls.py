from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home),
    path('form/',views.form_view,name='form'),
    path('booking',views.booking),
    path('update/<int:pk>',views.update,name='update'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('history/<int:pk>',views.history,name='history')
    
]