from django.contrib import admin

# Register your models here.

from .models import User
admin.site.register(User)

from .models import Group
admin.site.register(Group)

from .models import Product
admin.site.register(Product)

from .models import DailyOrder
admin.site.register(DailyOrder)

from .models import Combo
admin.site.register(Combo)

from .models import Components
admin.site.register(Components)

from .models import InventoryRecords
admin.site.register(InventoryRecords)