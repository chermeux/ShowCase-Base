"""
Admin - app product - display in djangoadmin models
"""
############################ Import, Librairies etc ##############################
from django.contrib import admin
from product.models import Product

admin.site.register(Product)
