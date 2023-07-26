"""
Librairies
"""
from django.urls import path
from product.views import v_product

urlpatterns = [
    path('', v_product, name="ProductHome"),
]
