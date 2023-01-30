from codecs import unicode_escape_decode
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def create_product(request):
    if(request.method == 'POST'):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')
    
        if Product.objects.filter(name=pName):
            return render(request, 'create_product.html')

        else:
            if pGroup_name == '':
                pGroup_name = 'None'
            Product.objects.create(name=pName, price=pPrice, target_level=pTarget_level, units_per_order=pUnits_per_order, group_name=pGroup_name, unit_of_measurement=pUnit_of_measurement)
            return redirect('home')

    else:
        return render(request, 'create_product.html')

def view_product(request, pk):
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'p':p})

def update_product(request, pk):
    if(request.method == "POST"):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')
    
        Product.objects.filter(pk=pk).update(name=pName, price=pPrice, target_level=pTarget_level, units_per_order=pUnits_per_order, group_name=pGroup_name, unit_of_measurement=pUnit_of_measurement)
        return redirect('view_product', pk=pk)

    else:
        p = get_object_or_404(Product, pk=pk)
        return render(request, 'update_product.html', {'p':p})

def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('home')