"""
Librairies
"""
from django.shortcuts import render


def index(request):
    """
    Index programm broadcast index.html file
    """
    return render(request, "ShowCase/index.html")
