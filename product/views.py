"""
Librairies
"""
from django.shortcuts import render

# Create your views here.
def v_product(request):
    """
    Product page to display Product thanks to ProductMain.html file
    """
    return render(request, "Product/ProductMain.html")
