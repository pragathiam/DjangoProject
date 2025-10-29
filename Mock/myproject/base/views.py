from django.shortcuts import render
from django.http import HttpResponse
from base.models import StudentsModel

# Create your views here.
def students(request):
    model_instance=StudentsModel.objects.all()
    serialized_pydata