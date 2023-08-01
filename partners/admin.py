"""
Admin - app partners - display in djangoadmin models
"""
############################ Import, Librairies etc ##############################
from django.contrib import admin
from partners.models import Partner

admin.site.register(Partner)
