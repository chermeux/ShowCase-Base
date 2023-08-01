"""
URLS app product, CRUD
"""

############################# Libraries, views used for urls #############################
from django.urls import path
from product.views import r_products, c_product, d_product, u_product

########################### URLS, Organized in the order of CRUD #########################
urlpatterns = [
    path('create/', c_product, name="Product_c"),
    path('', r_products, name="Products_r"),
    path('update/<str:id_partner>', u_product, name="Product_u"),
    path('delete/<str:id_partner>', d_product, name="Product_d"),
]
