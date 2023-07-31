"""
Forms - app partners - Rule : One Form for One Model
"""

from django.forms import ModelForm
from partners.models import Partner

class PartnerForm(ModelForm):
    """
    Form from The Partner DataBase
    """
    class Meta:
        """
        Form Definition for PartnerForm
        """
        model = Partner
        fields = ["name", "description", "webSite", "logo"]

        def public_method_1(self):
            """
            Implementation of public method 1 for the linter
            """
        def public_method_2(self):
            """
            Implementation of public method 3 for the linter
            """
