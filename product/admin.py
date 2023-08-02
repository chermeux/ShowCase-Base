"""
Admin - app product - display in djangoadmin models
"""
############################ Import, Librairies etc ##############################
from django.contrib import admin
from product.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
