from django.contrib import admin
from .models import Category
from .models import Unit
from .models import Item
from .models import Supplier
from .models import Order
from .models import Employee

# Register your models here.
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Employee)