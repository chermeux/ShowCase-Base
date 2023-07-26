"""
Librairies
"""
from django.db import models

class Partner(models.Model):
    """
    Model for a Partner
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.FileField()
    description = models.CharField(max_length=100)
    webSite = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
