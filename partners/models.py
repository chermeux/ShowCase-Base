"""
Librairies
"""
from django.core.validators import URLValidator
from django.db import models


class Partner(models.Model):
    """
    Model for a Partner
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to="images/")
    description = models.CharField(max_length=255)
    webSite = models.URLField(max_length=200,
                              validators=[URLValidator(schemes=['https'], regex=None, code=None)])

    def __str__(self):
        return str(self.name)
