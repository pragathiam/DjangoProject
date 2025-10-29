from django.urls import path
from auth_user import views

urlpatterns=[
    path('login_',views.login_,name='login_'),
    path('regitser',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout_,name='logout_'),
    path('change_password',views.change_password,name='change_password'),
    path('update_det/<int:pk>',views.Update_User_details,name='update_user_details'),
]