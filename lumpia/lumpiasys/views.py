from codecs import unicode_escape_decode
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime

# Create your views here.

def edit_productlist(request):
    current_datetime = datetime.now().date() 
    products = Product.objects.all()
    return render(request, 'edit_productlist.html', {'current_datetime':current_datetime, 'products':products})

def create_product(request):
    current_datetime = datetime.now() 
    if(request.method == 'POST'):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')
    
        if Product.objects.filter(name=pName):
            return render(request, 'create_product.html', {'current_datetime':current_datetime})

        else:
            if pGroup_name == '':
                pGroup_name = 'None'
            Product.objects.create(name=pName, price=pPrice, target_level=pTarget_level, units_per_order=pUnits_per_order, group_name=pGroup_name, unit_of_measurement=pUnit_of_measurement)
            return redirect('home')

    else:
        return render(request, 'create_product.html', {'current_datetime':current_datetime})

def view_product(request, pk):
    current_datetime = datetime.now().date() 
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'current_datetime':current_datetime,'p':p})

def update_product(request, pk):
    current_datetime = datetime.now().date()  
    if(request.method == 'POST'):
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
        return render(request, 'update_product.html', {'current_datetime':current_datetime, 'p':p})

def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('home')

def inventory_tally(request):
    inventories = Inventory.objects.all()

    if(request.method == "POST"):
        counted_units = request.POST.get('counted_units')
        itRemarks = request.POST.get('remarks')

    return render(request, 'inventory_tally.html', {'inventories':inventories})

def import_sales(request):
    products = Product.objects.all()

    if(request.method == "POST"):
        for i in products:
            pOrders = request.POST.get('order')
            cUnits_sold = pOrders * i.units_per_order

    return render(request, 'import_sales.html', {'products':products})

def remaining_inventory(request):
    current_datetime = datetime.now().date() 
    return render(request, 'remaining_inventory.html')

def home(request):
    current_datetime = datetime.now().date() 
    return render(request, 'home.html',  {'current_datetime':current_datetime})