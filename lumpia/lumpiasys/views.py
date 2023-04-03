from codecs import unicode_escape_decode
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime

# Create your views here.

def edit_productlist(request):
    current_date = datetime.now().date() 
    products = Product.objects.all()
    return render(request, 'edit_productlist.html', {'current_date':current_date, 'products':products})

def create_product(request):
    current_date = datetime.now().date()
    if(request.method == 'POST'):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')
    
        if Product.objects.filter(name=pName):
            return render(request, 'create_product.html', {'current_date':current_date})

        else:
            if pGroup_name == ' ':
                pGroup_name = 'None'
            Product.objects.create(name=pName, price=pPrice, target_level=pTarget_level, units_per_order=pUnits_per_order, group_name=pGroup_name, unit_of_measurement=pUnit_of_measurement)
            return redirect('home')

    else:
        return render(request, 'create_product.html', {'current_date':current_date})

def view_product(request, pk):
    current_date = datetime.now().date() 
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'current_date':current_date,'p':p})

def update_product(request, pk):
    current_date = datetime.now().date()  
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
        return render(request, 'update_product.html', {'current_date':current_date, 'p':p})

def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('home')

def inventory_tally(request):
    current_date = datetime.now().date()
    orders = DailyOrder.objects.all()

    return render(request, 'inventory_tally.html', {'current_date':current_date, 'orders':orders})

def import_sales(request):
    current_date = datetime.now().date()
    products = Product.objects.all()
    return render(request, 'import_sales.html', {'current_date':current_date, 'products':products})

def remaining_inventory(request):
    current_date = datetime.now().date()
    return render(request, 'remaining_inventory.html', {'current_date':current_date})

def home(request):
    current_date = datetime.now().date() 
    return render(request, 'home.html',  {'current_date':current_date})

def confirm_sales(request): #used for import sales
    current_date = datetime.now().date()
    products = Product.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        counter = 0
        for item in products:
            iName = item.getName()
            tprice = item.getPrice()
            iUPO = item.getUnitsPerOrder()
            cUnits = cUnitsList[counter]
            uSold = int(cUnits) * int(iUPO)
            DailyOrder.objects.create(date = current_date, item_name = iName, total_price = tprice, units_sold = uSold)
            counter += 1

        return redirect('inventory_tally')

def confirm_inventory(request):
    current_date = datetime.now().date()
    products = Product.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        cRemarksList = request.POST.getlist('remarks')
        counter = 0
        for item in products:
            iName = item.getName()
            rInventory = cUnitsList[counter]
            iRemarks = cRemarksList[counter]
            Inventory.objects.create(product_name = iName, date = current_date, remaining_inventory = rInventory, units_sold = 0, remarks = iRemarks)
            counter += 1

        return redirect('remaining_inventory')