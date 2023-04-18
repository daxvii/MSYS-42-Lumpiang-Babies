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
    stocks = models.IntegerField()
    target_level = models.IntegerField()
    units_per_order = models.IntegerField()
    group_name = models.CharField(max_length=20)
    unit_of_measurement = models.CharField(max_length=20)
    objects = models.Manager()

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
        return f"pk: {self.pk}: {self.name}, {self.price}, {self.stock}, {self.target_level}, {self.units_per_order}, {self.group_name}, {self.unit_of_measurement}"

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
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    units_sold = models.IntegerField()
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
        db_table = 'Daily_Order'

class Components(models.Model):
    # single_item_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    # combo_item_name = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_per_item = models.IntegerField()
    units_of_measurement = models.CharField(max_length=20)

    class Meta:
        db_table = 'Components'