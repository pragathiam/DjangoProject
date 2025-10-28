from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
api_keys='cba89ac28a03b715a00c1766491d984b'

def home(request):
    # read (get)

    if request.method == 'POST':

        city_name='goa'
        resp_data=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_keys}')
        py_data=resp_data.json()
        return render(request,'home.html',{'data':py_data})