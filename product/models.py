"""
Model Page about product app
"""

############################ Import, Librairies etc ##############################
from django.db import models

############################ Models ##############################
class Category(models.Model):
    """
    Model for a category in oder to organize a product if we want
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    """
    Model for a Product
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to="images/")
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)
