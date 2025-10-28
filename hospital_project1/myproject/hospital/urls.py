from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/update/<int:id>/', views.update_patient, name='update_patient'),
    path('patients/delete/<int:id>/', views.delete_patient, name='delete_patient'),

    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/update/<int:id>/', views.update_doctor, name='update_doctor'),
    path('doctors/delete/<int:id>/', views.delete_doctor, name='delete_doctor'),
]
