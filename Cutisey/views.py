from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'Cutisey/index.html')


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

def productView(request):
    return render(request, 'Cutisey/prodView.html')

