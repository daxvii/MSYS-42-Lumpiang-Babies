from ssl import create_default_context
from unicodedata import name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = 'Accounts'
        permissions = (("Can view remaining inventory", "Admin"),)

class Group(models.Model):
    group_id = models.CharField(max_length=30)
    objects = models.Manager()

    def getGroupName(self):
        return self.group_id

    def __str__(self):
        return f"{self.group_id}"

    class Meta:
        db_table = 'Groups'

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stocks = models.DecimalField(max_digits=10, decimal_places=2)
    target_level = models.DecimalField(max_digits=10, decimal_places=2)
    units_per_order = models.DecimalField(max_digits=10, decimal_places=2)
    stocks = models.DecimalField(max_digits=10, decimal_places=2)
    target_level = models.DecimalField(max_digits=10, decimal_places=2)
    units_per_order = models.DecimalField(max_digits=10, decimal_places=2)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
    unit_of_measurement = models.CharField(max_length=20)


    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price

    def getStocks(self):
        return self.stocks

    def getTargetLevel(self):
        return self.target_level

    def getUnitsPerOrder(self):
        return self.units_per_order

    def getGroupName(self):
        return self.group_name

    def getUnitOfMeasurement(self):
        return self.unit_of_measurement

    def getPk(self):
        return self.pk

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'Products'
        permissions = [
                (
                    "set_published_status",
                    "Can set the status of the post to either publish or not"
                )
            ]
        permissions = [(("Can view remaining inventory"), ("Admin"),)]

class DailyOrder(models.Model):
    date = models.DateField()
    item_name = models.CharField(max_length=30)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    units_sold = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    objects = models.Manager()

    def getDate(self):
        return self.date

    def getItemName(self):
        return self.item_name
    
    def getItemPrice(self):
        return self.item_price

    def getUnitsSold(self):
        return self.units_sold

    def getRemarks(self):
        return self.remarks
    
    def getPk(self):
        return self.pk

    def __str__(self):
        return f"{self.date}, {self.item_name}, {self.item_price}, {self.units_sold}, {self.remarks}"

    class Meta:
        db_table = 'Daily_orders'

class Combo(models.Model):
    combo_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    group_name = models.CharField(max_length=30)
    objects = models.Manager()

    def getName(self):
        return self.combo_name

    def getPrice(self):
        return self.price
    
    def getGroupName(self):
        return self.group_name

    def getPk(self):
        return self.pk

    def __str__(self):
        return f"{self.combo_name}"

    class Meta:
        db_table = 'Combos'

class Components(models.Model):
    combo_name = models.ForeignKey(Combo, on_delete=models.CASCADE, default='')
    item_name = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    quantity_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()

    def getComboName(self):
        return self.combo_name

    def getItemName(self):
        return self.item_name

    def getQuantity(self):
        return self.quantity_per_item

    def getPk(self):
        return self.pk

    def __str__(self):
        return f"{self.combo_name}, {self.item_name}, {self.quantity_per_item}"

    class Meta:
        db_table = 'Components'

class InventoryRecords(models.Model):
    date = models.DateField()
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    stocks = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()

    def getDate(self):
        return self.date

    def getProductName(self):
        return self.product_name

    def getStocks(self):
        return self.stocks

    def getPk(self):
        return self.pk

    def __str__(self):
        return f"{self.date}, {self.product_name}, {self.stocks}"

    class Meta:
        db_table = 'Inventory_records'