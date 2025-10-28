from django.urls import path
from . import views
urlpatterns=[
    path('',views.flight),
    path('status/',views.status,name='status'),
    path('time/',views.time,name='time'),
    path('destination/',views.destination,name='destination'),
    path('update/<int:pk>',views.update,name='update'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('history/<int:pk>',views.history,name='history')
    
]