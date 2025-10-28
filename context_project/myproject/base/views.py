from django.shortcuts import render

# Create your views here.
def home(request):
    data='this is homepage data send through context'
    return render(request,'home.html',{'data':data})
    #or 
    # context={'data':data}
    #return render(request,'home.html',context)


def about(request):
    data='this is about page data send through context'
    return render(request,'about.html',{'data':data})

def mobiles(request):
    data='this is mobiles data send through context'
    return render(request,'mobiles.html',{'data':data})

def laptops(request):
    data='this is laptops data send through context'
    return render(request,'laptops.html',{'data':data})

