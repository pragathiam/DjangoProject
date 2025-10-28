from django.shortcuts import render
from base.models import Fruits
from django.db.models import Q

# Create your views here.
def home(request):
    print(request.GET) 

    if 'q' in request.GET:
        q=request.GET['q']
        print(q)
        all_data=Fruits.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    else:    
         all_data=Fruits.objects.all()

    return render(request,'home.html',{'all_data':all_data})