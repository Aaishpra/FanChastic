from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil

# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    n=len(products)
    nSlides = n//4 + ceil((n/4)+(n//4))
    params = {'no_of_slides': nSlides,'range':range(1,nSlides),'product': products}
    return render(request, 'Cutisey/index.html',params)


def about(request):
    return render(request, 'Cutisey/about.html')


def contact(request):
    return render(request, 'Cutisey/contact.html')

def tracker(request):
    return render(request, 'Cutisey/tracker.html')
    
def search(request):
    return render(request, 'Cutisey/search.html')

def checkout(request):
    return render(request, 'Cutisey/checkout.html')

def productView(request, myid):
# Fetch the product using the id
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, 'Cutisey/productView.html', {'product':product[0]})

def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'Cutisey/contact.html')