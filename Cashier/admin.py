from django.contrib import admin
from .models import User, Product, Transaction_items, Transaction


# Register your models here.
admin.site.register(Product)
admin.site.register(User)
