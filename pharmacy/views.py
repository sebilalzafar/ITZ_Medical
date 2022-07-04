from django.shortcuts import render
from pharmacy.models import *

# Create your views here.


def pharmacy(request):
    data = Medicine.objects.all()
    return render(request,'pharmacy/products.html', { 'data': data })
def cart(request):
    return render(request,'pharmacy/cart.html',)
