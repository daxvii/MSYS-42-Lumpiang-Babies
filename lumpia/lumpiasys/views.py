from codecs import unicode_escape_decode
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def edit_productlist(request):
    products = Product.objects.all()
    combos = Combo.objects.all()
    groups = Group.objects.all()
    
    return render(request, 'edit_productlist.html', {'products':products, 'groups':groups, 'combos':combos})


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
            return render(request, 'create_product.html', {'g':g})

        else:
            product_group = get_object_or_404(Group, group_id=str(pGroup_name))
            Product.objects.create(name=pName, price=pPrice, stocks=pStocks, target_level=pTarget_level,units_per_order=pUnits_per_order, group_name=product_group, unit_of_measurement=pUnit_of_measurement)
            return redirect('edit_productlist')

    else:
        return render(request, 'create_product.html', {'g':g})


def view_product(request, pk):
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'p':p})


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
        Product.objects.filter(pk=pk).update(name=pName, price=pPrice, stocks=pStocks, target_level=pTarget_level, units_per_order=pUnits_per_order, group_name=product_group, unit_of_measurement=pUnit_of_measurement)
        return redirect('view_product', pk=pk)

    else:
        p = get_object_or_404(Product, pk=pk)
        pg = Product.objects.get(pk=pk)
        product_group_name = pg.getGroupName()
        return render(request, 'update_product.html', {'p':p, 'g':g, 'product_group_name':product_group_name})


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
    return render(request, 'edit_grouplist.html', {'groups':groups})


def view_group(request, pk):
    g = get_object_or_404(Group, pk=pk)
    return render(request, 'view_group.html', {'g':g})


def update_group(request, pk):
    if (request.method == 'POST'):
        gName = request.POST.get('group_id')

        Group.objects.filter(pk=pk).update(group_id=gName)
        return redirect('view_group', pk=pk)

    else:
        g = get_object_or_404(Group, pk=pk)
        return render(request, 'update_group.html', {'g':g})


def delete_group(request, pk):
    Group.objects.filter(pk=pk).delete()
    return redirect('edit_grouplist')


def create_combo(request):
    p = Product.objects.all()
    g = Group.objects.all()
    if (request.method == 'POST'):
        cName = request.POST.get('cName')
        gName = request.POST.get('gName')
        cPrice = request.POST.get('price')
        itemList = request.POST.getlist('itemname')
        unitList = request.POST.getlist('unit')
        counter = 0

        if Combo.objects.filter(combo_name=cName):
            return render(request, 'create_combo.html')

        else:
            Combo.objects.create(combo_name=cName, price=cPrice, group_name=gName)
            combo_key = get_object_or_404(Combo, combo_name=str(cName))
            while counter != len(itemList):
                item = itemList[counter]
                unit = unitList[counter]
                item_key = get_object_or_404(Product, name=item)
                Components.objects.create(combo_name=combo_key, item_name=item_key, quantity_per_item=unit)
                counter += 1
            return redirect('edit_productlist')

    else:
        return render(request, 'create_combo.html', {'p':p, 'g':g} )


def view_combo(request, pk):
    c = get_object_or_404(Combo, pk=pk)
    cId = str(c.getPk())
    cComponents = Components.objects.raw("SELECT * FROM components WHERE components.combo_name_id = " + cId)
    return render(request, 'view_combo.html', {'c': c, 'cComponents':cComponents})


def update_combo(request, pk):
    p = Product.objects.all()
    g = Group.objects.all()
    c = get_object_or_404(Combo, pk=pk)
    cId = str(c.getPk())

    if (request.method == 'POST'):
        cName = request.POST.get('cName')
        gName = request.POST.get('gName')
        cPrice = request.POST.get('price')
        itemList = request.POST.getlist('itemname')
        unitList = request.POST.getlist('unit')
        counter = 0

        Combo.objects.filter(pk=pk).update(combo_name=cName, price=cPrice, group_name=gName)
        Components.objects.filter(combo_name=cId).delete()

        for i in itemList:
            item = itemList[counter]
            unit = unitList[counter]
            item_key = get_object_or_404(Product, name=item)
            Components.objects.create(combo_name=c, item_name=item_key, quantity_per_item=unit)
            counter += 1

        return redirect('view_combo', pk=pk)

    else:
        cComponents = Components.objects.raw("SELECT * FROM components WHERE components.combo_name_id = " + cId)
        combogrp = Combo.objects.get(pk=pk)
        c_group_name = combogrp.getGroupName()
        return render(request, 'update_combo.html', {'p':p, 'g':g, 'c':c, 'c_group_name':c_group_name, 'cComponents':cComponents})


def delete_combo(request, pk):
    Combo.objects.filter(pk=pk).delete()
    return redirect('edit_productlist')

def import_sales(request):
    products = Product.objects.all()
    groups = Group.objects.all()
    combos = Combo.objects.all()
    components = Components.objects.all()
    return render(request, 'import_sales.html', {'products': products, 'groups': groups, 'combos': combos, 'components': components})


def confirm_sales(request):  # used for import sales
    current_date = datetime.now().date()
    products = Product.objects.all()
    combos = Combo.objects.all()
    components = Components.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        cComboUnitsList = request.POST.getlist('counted_combo_units')
        pCounter = 0
        cCounter = 0

        for item in products:
            iName = item.getName()
            iprice = item.getPrice()
            iUPO = item.getUnitsPerOrder()
            cUnits = cUnitsList[pCounter]
            uSold = int(cUnits) * int(iUPO)
            DailyOrder.objects.create(date=current_date, item_name=iName, item_price=iprice, units_sold=uSold, remarks='')

            rStocks = item.getStocks()
            fStocks = rStocks - uSold
            Product.objects.filter(name=iName).update(stocks=fStocks)
            pCounter += 1
        
        for item in combos:
            iName = item.getName()
            iprice = item.getPrice()
            uSold = cComboUnitsList[cCounter]
            DailyOrder.objects.create(date=current_date, item_name=iName, item_price=iprice, units_sold=uSold, remarks='')

            iPk = item.getPk()
            cComponents = Components.objects.filter(combo_name=iPk)
            for c in cComponents:
                itemName = c.getItemName()
                itemRef = get_object_or_404(Product, name=itemName)
                rStocks = itemRef.getStocks()
                uSold = c.getQuantity()
                fStocks = rStocks - uSold
                Product.objects.filter(name=itemName).update(stocks=fStocks)
            cCounter += 1

        return redirect('inventory_tally')


def inventory_tally(request):
    products = Product.objects.all()
    groups = Group.objects.all()

    return render(request, 'inventory_tally.html', {'products':products, 'groups':groups})


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
    groups = Group.objects.all()
    for i in products:
        iName = i.getName()
        j = Product.objects.filter(name=iName).last()
        current_inventory.append(j)

    return render(request, 'remaining_inventory.html', {'products':products, 'groups':groups})
