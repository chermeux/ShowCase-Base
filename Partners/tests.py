"""
    Librairies
"""
from django.test import TestCase, Client
from pytest_django.asserts import assertTemplateUsed


class ViewsTestCaseIndex(TestCase):
    """
        Class for all tests about PartnersMain (page to display partners...) in Partners
    """
    def v_basics(self):
        """
        Test Partners Page - Function PartnersMain - status_code=200 and good template
        """
        client = Client()
        response = client.get("/partners/")
        self.assertEqual(response.status_code, 200)
        assertTemplateUsed(response, "Partners/PartnersMain.html")
