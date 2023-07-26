"""
Librairies
"""
from django.shortcuts import render

# Create your views here.
def v_parteners(request):
    """
    Partners page to display Partners thanks to PartnersMain.html file
    """
    return render(request, "Partners/PartnersMain.html")
