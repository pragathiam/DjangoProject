from django.shortcuts import render,redirect
from base.models import Products
from base.models 

# Create your views here.
def home(request):
    all_products=Products.objects.all()
    return render(request,'home.html',{'all_products':all_products})

def add_products(request):

    if request.method == 'POST':
        p_category=request.POST['p_category']

        return redirect('home')

    return render(request,'add_products.html')

@login_required(login_url='login_')
def add_to_cart(request,pk):

    pro=Products.objects.get(id=pk)
    
    CartModel.objects.create(
        p_category=pro.p_category,
        p_name=pro.p_name,
        p_desc=pro.p_desc,
        p_price=pro.p_price,       
    )  
    return redirect('cart')    

def cart(request):
    all_cart_products=CartModel.objects.all()
    return render(request,'cart.html',{'all_cart_products':all_cart_products})

def remove(request):
    return render(request,)