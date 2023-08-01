"""
Model Page about product app
"""

############################ Import, Librairies etc ##############################
from django.db import models

############################ Models ##############################
class Product(models.Model):
    """
    Model for a Partner
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.FileField(upload_to="images/")
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)
