"""
    Librairies
"""
from django.test import TestCase, Client
from pytest_django.asserts import assertTemplateUsed


class ViewsTestCaseProductMain(TestCase):
    """
        Class for all tests about ProductMain (page to display partners...) in Product
    """
    def test_v_basics(self):
        """
        Test Product Page - Function ProductMain - status_code=200 and good template
        """
        client = Client()
        response = client.get("/product/")
        self.assertEqual(response.status_code, 200)
        assertTemplateUsed(response, "Product/ProductMain.html")
