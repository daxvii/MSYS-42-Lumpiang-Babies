from codecs import unicode_escape_decode
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime

# Create your views here.


def home(request):
    current_date = datetime.now().date()
    return render(request, 'home.html',  {'current_date': current_date})

def edit_productlist(request):
    current_date = datetime.now().date()
    products = Product.objects.all()
    return render(request, 'edit_productlist.html', {'current_date': current_date, 'products': products})


def create_product(request):
    current_date = datetime.now().date()
    if (request.method == 'POST'):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pStocks = request.POST.get('stocks')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')

        if Product.objects.filter(name=pName):
            return render(request, 'create_product.html', {'current_date': current_date})

        else:
            Product.objects.create(name=pName, price=pPrice, stocks=pStocks, target_level=pTarget_level,units_per_order=pUnits_per_order, group_name=pGroup_name, unit_of_measurement=pUnit_of_measurement)
            return redirect('edit_productlist')

    else:
        return render(request, 'create_product.html', {'current_date': current_date})


def view_product(request, pk):
    current_date = datetime.now().date()
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'current_date': current_date, 'p': p})


def update_product(request, pk):
    current_date = datetime.now().date()
    if (request.method == 'POST'):
        pName = request.POST.get('name')
        pPrice = request.POST.get('price')
        pStocks = request.POST.get('stocks')
        pTarget_level = request.POST.get('target_level')
        pUnits_per_order = request.POST.get('units_per_order')
        pGroup_name = request.POST.get('group_name')
        pUnit_of_measurement = request.POST.get('unit_of_measurement')

        Product.objects.filter(pk=pk).update(name=pName, price=pPrice, stocks=pStocks, target_level=pTarget_level,units_per_order=pUnits_per_order, group_name=pGroup_name, unit_of_measurement=pUnit_of_measurement)
        return redirect('view_product', pk=pk)

    else:
        p = get_object_or_404(Product, pk=pk)
        return render(request, 'update_product.html', {'current_date': current_date, 'p': p})


def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('edit_productlist')


def import_sales(request):
    current_date = datetime.now().date()
    products = Product.objects.all()
    return render(request, 'import_sales.html', {'current_date': current_date, 'products': products})

def confirm_sales(request):  # used for import sales
    current_date = datetime.now().date()
    products = Product.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        counter = 0
        # for item in products:
        #     iName = item.getName()
        #     iprice = item.getPrice()
        #     iUPO = item.getUnitsPerOrder()
        #     cUnits = cUnitsList[counter]
        #     uSold = int(cUnits) * int(iUPO)
        #     # rInventory = Inventory.objects.filter(product_name = iName).last()
        #     rStocks = item.getStock()
        #     fStocks = rStocks - uSold
        #     Product.objects.create(date=current_date, item_name=iName, total_price=tprice, units_sold=uSold, final_stocks=fStocks)
        #     counter += 1

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
    current_date = datetime.now().date()
    products = Product.objects.all()

    return render(request, 'inventory_tally.html', {'current_date': current_date, 'products': products})

def confirm_inventory(request): #used for inventory tally
    current_date = datetime.now().date()
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
    current_date = datetime.now().date()
    current_inventory = []
    products = Product.objects.all()
    for i in products:
        iName = i.getName()
        j = Product.objects.filter(name=iName).last()
        current_inventory.append(j)

    return render(request, 'remaining_inventory.html', {'current_date': current_date, 'products': products})
