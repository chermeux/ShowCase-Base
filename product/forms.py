"""
Forms - app product - Rule : One Form for One Model
"""
############################ Import, Librairies etc ##############################
from django.forms import ModelForm
from product.models import Product, Category

############################ Forms ##############################
class CategoryForm(ModelForm):
    """
    Form from The Product DataBase
    """
    class Meta:
        """
        Form Definition for ProductForm
        """
        model = Category
        fields = ["name", "description"]

        def public_method_1(self):
            """
            Implementation of public method 1 for the linter
            """
        def public_method_2(self):
            """
            Implementation of public method 3 for the linter
            """

class ProductForm(ModelForm):
    """
    Form from The Product DataBase
    """
    class Meta:
        """
        Form Definition for ProductForm
        """
        model = Product
        fields = ["title", "description", "category", "image"]

        def public_method_1(self):
            """
            Implementation of public method 1 for the linter
            """
        def public_method_2(self):
            """
            Implementation of public method 3 for the linter
            """
