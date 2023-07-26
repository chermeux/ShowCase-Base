"""
Librairies
"""
# pylint: disable=E0401
from django.urls import path
from show_case.views import index

urlpatterns = [
    path('', index, name ="HomePage"),
]
