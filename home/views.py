# Create your views here.
from django.shortcuts import render
from .models import Nut

# Create your views here.
def index(request):
    Nuts = Nut.objects.all()
    data = {
        'nuts' : Nuts
    }
    return render(request, 'home/index.html', data)

def products(request):
    return render(request, 'home/products.html')

def register(request):
    return render(request, 'home/register.html')

def login(request):
    return render(request, 'home/login.html')