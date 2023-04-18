from django.contrib import admin

# Register your models here.

from .models import Product
admin.site.register(Product)

from .models import DailyOrder
admin.site.register(DailyOrder)