from django.urls import path
from base import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('update/<int:pk>',views.update,name='update'),
    path('deleted_/<int:pk>',views.deleted_,name='deleted_'),
    path('history',views.history,name='history'),
    path('restore/<int:pk>',views.restore,name='restore'),
    path('delete_all_history',views.delete_all_history,name='delete_all_history'),
    path('delete_history/<int:pk>',views.delete_history,name='delete_history'),
    path('restore_all',views.restore_all,name='restore_all'),
    path('confirmdelete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    
]