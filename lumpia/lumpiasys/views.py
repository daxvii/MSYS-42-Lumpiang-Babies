from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
 
def signup(request):
    if request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = form.save()
            login(request, user)
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def home(request):
    current_inventory = []
    products = Product.objects.all()
    groups = Group.objects.all()
    for i in products:
        iName = i.getName()
        j = Product.objects.filter(name=iName).last()
        current_inventory.append(j)

    #return render(request, 'remaining_inventory.html', {'products':products, 'groups':groups})
    return render(request, 'home.html', {'products':products, 'groups':groups})

@login_required
def edit_productlist(request):
    products = Product.objects.all()
    combos = Combo.objects.all()
    groups = Group.objects.all()
    
    return render(request, 'edit_productlist.html', {'products':products, 'groups':groups, 'combos':combos})

@login_required
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

@login_required
def view_product(request, pk):
    p = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'p':p})

@login_required
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

@login_required
def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('edit_productlist')

@login_required
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

@login_required
def edit_grouplist(request):
    groups = Group.objects.all()
    return render(request, 'edit_grouplist.html', {'groups':groups})

@login_required
def view_group(request, pk):
    g = get_object_or_404(Group, pk=pk)
    return render(request, 'view_group.html', {'g':g})

@login_required
def update_group(request, pk):
    if (request.method == 'POST'):
        gName = request.POST.get('group_id')

        Group.objects.filter(pk=pk).update(group_id=gName)
        return redirect('view_group', pk=pk)

    else:
        g = get_object_or_404(Group, pk=pk)
        return render(request, 'update_group.html', {'g':g})

@login_required
def delete_group(request, pk):
    Group.objects.filter(pk=pk).delete()
    return redirect('edit_grouplist')

@login_required
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

@login_required
def view_combo(request, pk):
    c = get_object_or_404(Combo, pk=pk)
    cId = str(c.getPk())
    cComponents = Components.objects.raw("SELECT * FROM components WHERE components.combo_name_id = " + cId)
    return render(request, 'view_combo.html', {'c': c, 'cComponents':cComponents})

@login_required
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

@login_required
def delete_combo(request, pk):
    Combo.objects.filter(pk=pk).delete()
    return redirect('edit_productlist')

@login_required
def import_sales(request):
    products = Product.objects.all()
    groups = Group.objects.all()
    combos = Combo.objects.all()
    components = Components.objects.all()
    compLength = len(components)
    print(compLength)
    totalComp = []

    # for i in range(compLength):
    #     compSum = []
    #     for component in components:
    #         componentQty = component.getQuantity()
    #         compSum.append(componentQty)
    #     totalComp
        


    # for component in components:
    #     if Combo.objects.get(pk=component) == Components.

    current_date = datetime.now().date()
    boolean = DailyOrder.objects.filter(date=current_date).exists()

    return render(request, 'import_sales.html', {'products': products, 'groups': groups, 'combos': combos, 'components': components, 'boolean': boolean})

@login_required
def confirm_sales(request):  # used for import sales
    current_date = datetime.now().date()
    products = Product.objects.all()
    combos = Combo.objects.all()
    
    # components = Components.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        cComboUnitsList = request.POST.getlist('counted_combo_units')
        pCounter = 0
        cCounter = 0

        if DailyOrder.objects.filter(date=current_date).exists():
            return render(request, 'home.html')

        else:
            for item in products:
                iName = item.getName()
                iprice = item.getPrice()
                iUPO = item.getUnitsPerOrder()
                cUnits = cUnitsList[pCounter]
                uSold = int(cUnits) * int(iUPO)
                DailyOrder.objects.create(date=current_date, item_name=iName, item_price=iprice, units_sold=uSold, remarks='')

                rStocks = item.getStocks()
                fStocks = rStocks - uSold
                # Product.objects.filter(name=iName).update(stocks=fStocks)
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
                    uSold2 = c.getQuantity() * int(uSold)
                    fStocks = rStocks - uSold2
                    # Product.objects.filter(name=itemName).update(stocks=fStocks)
                cCounter += 1

            return redirect('inventory_tally')

@login_required
def inventory_tally(request):
    products = Product.objects.all()
    groups = Group.objects.all()

    current_date = datetime.now().date()
    booleanOrder = DailyOrder.objects.filter(date=current_date).exists()
    booleanTally = InventoryRecords.objects.filter(date=current_date).exists()

    return render(request, 'inventory_tally.html', {'products':products, 'groups':groups, 'booleanTally': booleanTally, 'booleanOrder': booleanOrder})

@login_required
def confirm_inventory(request): #used for inventory tally
    current_date = datetime.now().date()
    products = Product.objects.all()
    daily_orders = DailyOrder.objects.all()

    if (request.method == 'POST'):
        cUnitsList = request.POST.getlist('counted_units')
        RemarksList = request.POST.getlist('remarks')
        counter = 0

        if InventoryRecords.objects.filter(date=current_date).exists():
            return render(request, 'home.html')

        else:
            for item in products:
                iName = item.getName()
                iStocks = item.getStocks()
                iRemarks = RemarksList[counter]
                if iStocks != cUnitsList[counter]:
                    if RemarksList[counter] != '':
                        Product.objects.filter(name=iName).update(stocks = cUnitsList[counter]) 
                        DailyOrder.objects.filter(item_name=iName).update(remarks=iRemarks)
                product_key = get_object_or_404(Product, name=iName)
                fStocks = product_key.getStocks()
                InventoryRecords.objects.create(date=current_date, product_name=product_key, stocks=fStocks)
                counter += 1

            return redirect('remaining_inventory')

@login_required
def remaining_inventory(request):
    current_inventory = []
    products = Product.objects.all()
    groups = Group.objects.all()
    for i in products:
        iName = i.getName()
        j = Product.objects.filter(name=iName).last()
        current_inventory.append(j)

    return render(request, 'remaining_inventory.html', {'products':products, 'groups':groups})

@login_required
def view_inventory_records(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        inventory_records = InventoryRecords.objects.filter(date=date)
        return render(request, 'view_inventory_records.html', {'inventory_records': inventory_records})

    else:
        return render(request, 'view_inventory_records.html')
