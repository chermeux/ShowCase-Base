"""
Librairies
"""
from django.urls import path
from Partners.views import v_parteners

urlpatterns = [
    path('', v_parteners, name="PartnersHome"),
]
