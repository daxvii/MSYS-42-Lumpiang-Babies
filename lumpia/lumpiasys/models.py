from ssl import create_default_context
from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def __str__(self):
        return f"pk: {self.pk}: {self.username}, {self.password}"

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    target_level = models.IntegerField()
    units_per_order = models.IntegerField()
    group_name = models.CharField(max_length=20, blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=20)
    objects = models.Manager()

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price

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
        return f"pk: {self.pk}: {self.name}, {self.price}, {self.target_level}, {self.units_per_order}, {self.group_name}, {self.unit_of_measurement}"

class Combo(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    group_name = models.CharField(max_length=30)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
    
    def getGroupName(self):
        return self.group_name

    def getPk(self):
        return self.pk

    def __str__(self):
        return f"pk: {self.pk}: {self.name}, {self.price}, {self.group_name}"

class DailyOrder(models.Model):
    date = models.DateField()
    item_name = models.CharField(max_length=30)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    orders_sold = models.IntegerField()

    def getDate(self):
        return self.date

    def getItemName(self):
        return self.item_name
    
    def getTotalPrice(self):
        return self.total_price

    def getOrdersSold(self):
        return self.orders_sold
    
    def getPk(self):
        return self.pk

    def __str__(self):
        return f"{self.date}, {self.item_name}, {self.total_price}, {self.orders_sold}"

class Inventory(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    remaining_inventory = models.IntegerField()
    units_sold = models.IntegerField()
    remarks = models.CharField(max_length=100, blank=True, null=True)
    objects = models.Manager()

    def getName(self):
        return self.product_name.getName()

    def getDate(self):
        return self.date

    def getRemainingInventory(self):
        return self.remaining_inventory

    def getUnitsSold(self):
        return self.units_sold
    
    def getRemarks(self):
        return self.remarks

    def __str__(self):
        return f"{self.getName()}, {self.date}, {self.remaining_inventory}, {self.units_sold}, {self.remarks}"

class Components(models.Model):
    # single_item_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    # combo_item_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_per_item = models.IntegerField()
    units_of_measurement = models.CharField(max_length=20)