"""
URLS app partners, CRUD
"""

############################# Libraries, views used for urls #############################
from django.urls import path
from partners.views import r_partners, c_partner, d_partner, u_partner

########################### URLS, Organized in the order of CRUD #########################
urlpatterns = [
    path('create/', c_partner, name="Partner_c"),
    path('', r_partners, name="Partners_r"),
    path('update/<str:id_partner>', u_partner, name="Partner_u"),
    path('delete/<str:id_partner>', d_partner, name="Partner_d"),
]
