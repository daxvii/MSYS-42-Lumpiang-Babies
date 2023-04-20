from codecs import unicode_escape_decode
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, 'home.html')

def edit_productlist(request):
    products = Product.objects.all()
    return render(request, 'edit_productlist.html', {'products': products})


def create_product(request):
    g = Group.objects.all()
    if (request.method == 'POST'):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pStocks = request.POST.get('stocks')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')

        if Product.objects.filter(name=pName):
            return render(request, 'create_product.html')

        else:
            product_group = get_object_or_404(Group, group_id=str(pGroup_name))
            Product.objects.create(name=pName, price=pPrice, stocks=pStocks, target_level=pTarget_level,units_per_order=pUnits_per_order, group_name=product_group, unit_of_measurement=pUnit_of_measurement)
            return redirect('edit_productlist')

    else:
        return render(request, 'create_product.html', {'g': g})


def view_product(request, pk):
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'p': p})


def update_product(request, pk):
    g = Group.objects.all()
    if (request.method == 'POST'):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pStocks = request.POST.get('stocks')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')

        product_group = get_object_or_404(Group, group_id=str(pGroup_name))
        Product.objects.filter(pk=pk).update(name=pName, price=pPrice, stocks=pStocks, target_level=pTarget_level,units_per_order=pUnits_per_order, group_name=product_group, unit_of_measurement=pUnit_of_measurement)
        return redirect('view_product', pk=pk)

    else:
        p = get_object_or_404(Product, pk=pk)
        return render(request, 'update_product.html', {'p': p}, {'g': g})


def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('edit_productlist')


def create_group(request):
    if (request.method == 'POST'):
        gName = request.POST.get('group_name')

        if Group.objects.filter(group_id=gName):
            return render(request, 'create_group.html')

        else:
            Group.objects.create(group_id=gName)
            return redirect('edit_productlist')

    else:
        return render(request, 'create_group.html')


def edit_grouplist(request):
    groups = Group.objects.all()
    return render(request, 'edit_grouplist.html', {'groups': groups})


def view_group(request, pk):
    g = get_object_or_404(Group, pk=pk)
    return render(request, 'view_group.html', {'g': g})


def update_group(request, pk):
    if (request.method == 'POST'):
        gName = request.POST.get('group_id')

        Group.objects.filter(pk=pk).update(group_id=gName)
        return redirect('view_group', pk=pk)

    else:
        g = get_object_or_404(Group, pk=pk)
        return render(request, 'update_group.html', {'g': g})


def delete_group(request, pk):
    Group.objects.filter(pk=pk).delete()
    return redirect('edit_grouplist')


def import_sales(request):
    products = Product.objects.all()
    groups = Group.objects.all()
    return render(request, 'import_sales.html', {'products': products})


def confirm_sales(request):  # used for import sales
    current_date = datetime.now().date()
    products = Product.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        counter = 0

        for item in products:
            iName = item.getName()
            iprice = item.getPrice()
            iUPO = item.getUnitsPerOrder()
            cUnits = cUnitsList[counter]
            uSold = int(cUnits) * int(iUPO)
            DailyOrder.objects.create(date=current_date, item_name=iName, item_price=iprice, units_sold=uSold, remarks='')
            rStocks = item.getStocks()
            fStocks = rStocks - uSold
            Product.objects.filter(name=iName).update(stocks = fStocks)
            counter += 1

        return redirect('inventory_tally')


def inventory_tally(request):
    products = Product.objects.all()

    return render(request, 'inventory_tally.html', {'products': products})


def confirm_inventory(request): #used for inventory tally
    products = Product.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        RemarksList = request.POST.getlist('remarks')
        counter = 0
        for item in products:
            iName = item.getName()
            iStocks = item.getStocks()
            iRemarks = RemarksList[counter]
            if iStocks != cUnitsList[counter]:
                if RemarksList[counter] != '':
                    Product.objects.filter(name=iName).update(stocks = cUnitsList[counter])
            DailyOrder.objects.filter(item_name=iName).update(remarks=iRemarks)
            counter += 1

        return redirect('remaining_inventory')


def remaining_inventory(request):
    current_inventory = []
    products = Product.objects.all()
    for i in products:
        iName = i.getName()
        j = Product.objects.filter(name=iName).last()
        current_inventory.append(j)

    return render(request, 'remaining_inventory.html', {'products': products})
