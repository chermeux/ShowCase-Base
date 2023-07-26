"""
Librairies
"""
from django.urls import path
from Partners.views import PartnersMain

urlpatterns = [
    path('', PartnersMain, name="PartnersHome"),
]
