from django.shortcuts import render, redirect
from .models import Patient, Doctor

# Create your views here.
def home(request):
    return redirect('patient_list')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        disease = request.POST.get('disease')

        if name and age and gender and disease:
            Patient.objects.create(
                name=name,
                age=age,
                gender=gender,
                disease=disease )
            return redirect('patient_list')
        else:
            return render(request, 'hospital/add_patient.html', {'error': 'All fields are required.'})

    return render(request, 'hospital/add_patient.html')


def update_patient(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']
        patient.disease = request.POST['disease']
        patient.save()
        return redirect('patient_list')
    return render(request, 'hospital/update_patient.html', {'patient': patient})

def delete_patient(request, id):
    Patient.objects.get(id=id).delete()
    return redirect('patient_list')




def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')

        if name and specialization and phone:
            Doctor.objects.create(
                name=name,
                specialization=specialization,
                phone=phone)
            return redirect('doctor_list')
        else:
            return render(request, 'hospital/add_doctor.html', {'error': 'All fields are required.'})
    return render(request, 'hospital/add_doctor.html')


def update_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.specialization = request.POST['specialization']
        doctor.phone = request.POST['phone']
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'hospital/update_doctor.html', {'doctor': doctor})

def delete_doctor(request, id):
    Doctor.objects.get(id=id).delete()
    return redirect('doctor_list')