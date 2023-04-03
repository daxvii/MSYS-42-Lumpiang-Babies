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

    class Meta:
        db_table = 'User'

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    target_level = models.IntegerField()
    units_per_order = models.IntegerField()
    group_name = models.CharField(max_length=20)
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

    class Meta:
        db_table = 'Product'

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

    class Meta:
        db_table = 'Combo'

class DailyOrder(models.Model):
    date = models.DateField()
    item_name = models.CharField(max_length=30)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    units_sold = models.IntegerField()
    final_stocks = models.IntegerField()
    objects = models.Manager()

    def getDate(self):
        return self.date

    def getItemName(self):
        return self.item_name
    
    def getTotalPrice(self):
        return self.total_price

    def getUnitsSold(self):
        return self.units_sold

    def getFinalStocks(self):
        return self.final_stocks
    
    def getPk(self):
        return self.pk

    def __str__(self):
        return f"{self.date}, {self.item_name}, {self.total_price}, {self.units_sold}"

    class Meta:
        db_table = 'Daily_order'

class Inventory(models.Model):
    product_name = models.CharField(max_length=30)
    date = models.DateField()
    remaining_inventory = models.IntegerField()
    units_sold = models.IntegerField()
    remarks = models.CharField(max_length=100, blank=True, null=True)
    # inventory_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    objects = models.Manager()

    def getName(self):
        return self.product_name

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

    class Meta:
        db_table = 'Inventory'

class Components(models.Model):
    # single_item_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    # combo_item_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_per_item = models.IntegerField()
    units_of_measurement = models.CharField(max_length=20)

    class Meta:
        db_table = 'Components'