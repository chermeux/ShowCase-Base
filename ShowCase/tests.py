"""
    Librairies
"""
from django.test import TestCase, Client
from pytest_django.asserts import assertTemplateUsed


class ViewsTestCaseIndex(TestCase):
    """
        Class for all tests about index in ShowCase
    """
    def v_basics(self):
        """
        Test Index Page - Function ShowCase - status_code=200 and good template
        """
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        assertTemplateUsed(response, "ShowCase/index.html")
