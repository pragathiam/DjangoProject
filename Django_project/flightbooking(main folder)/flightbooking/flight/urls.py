from django.urls import path
from flight import views
urlpatterns=[
    path('flight',views.flight),
    path('status',views.status),
    path('time',views.time),
    path('destination',views.destination),
    path('update/<int:pk>',views.update,name='update'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('history/<int:pk>',views.history,name='history')
    
]