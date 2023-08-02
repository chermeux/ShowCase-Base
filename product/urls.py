"""
URLS app product, CRUD
"""

############################# Libraries, views used for urls #############################
from django.urls import path
from product.views import c_product, r_products, u_product, d_product
from product.views import c_category, r_categories, u_category, d_category

########################### URLS, Organized in the order of CRUD #########################
urlpatterns = [
    path('create/', c_product, name="Product_c"),
    path('', r_products, name="Products_r"),
    path('update/<str:id_product>', u_product, name="Product_u"),
    path('delete/<str:id_product>', d_product, name="Product_d"),
    path('category/create/', c_category, name="Category_c"),
    path('category/', r_categories, name="Categories_r"),
    path('category/update/<str:id_category>', u_category, name="Category_u"),
    path('category/delete/<str:id_category>', d_category, name="Category_d"),
]
