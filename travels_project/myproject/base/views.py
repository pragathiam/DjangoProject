from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
Travels_data=[
    {
        'id':1,
        'title':'Domestic Travel',
        'desc':'''
    this is all about Domestic Travel
    <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>    
'''
    },
    {
        'id':2,
        'title':'International Travel',
        'desc':'''
     this is all about International Travel 
    <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>
'''
    },
    {
        'id':3,
        'title':'Cruise Travel',
        'desc':'''
    this is all about Cruise Travel 
    <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>
'''
    },
    {
        'id':4,
        'title':'Train Travel',
        'desc':'''
    this is all about Train Travel
    <h2>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum quo minima maxime libero cumque a, aliquam quis perspiciatis. Harum ipsa temporibus iure laborum quae aperiam fugit placeat, aut in similique, cum, suscipit fugiat. Non doloribus nihil fuga quisquam impedit, dolorum perferendis dolore ducimus, itaque amet minus et totam tempore provident?</h2>
'''
    },
    
]
def Deals_and_offers(request):
    context={
        'data':Travels_data,
        'nav':True,
        'title':'thos is Deals_and_offers'
    }
    return render(request,'Deals_and_offers.html',context)

def read(request,pk):
    # print(pk)
    # print(type(pk))
    travel = None

    for i in Travels_data:
        # print(i['id']) 
        if i['id'] == pk:
           travel = i
           break
        #    print(i)
    if travel:
        context = {'Travel': travel}
    else:
        context = {'Travel': {'id': 'N/A', 'title': 'Not Found', 'desc': 'No details available'}}

    return render(request,'read.html',context)

def Destinations(request):
    return render(request,'Destinations.html')

def Holiday_package(request):
    return render(request,'Holiday_package.html')

def Hotels(request):
    return render(request,'Hotels.html')

def Support(request):
    return render(request,'Support.html')

def Read(request):
    return render(request,'Read.html')