# pylint: disable=E1101

"""
    Librairies
"""
from django.test import TestCase, Client
from pytest_django.asserts import assertTemplateUsed
from partners.models import Partner

class ViewsTestCaseIndex(TestCase):
    """
        Class for all tests about PartnersMain (page to display partners...) in Partners
    """
    def test_v_basics(self):
        """
        Test Partners Page - Function PartnersMain - status_code=200 and good template
        """
        client = Client()
        response = client.get("/partners/")
        self.assertEqual(response.status_code, 200)
        assertTemplateUsed(response, "Partners/PartnersMain.html")

class ModelTestCasePartner(TestCase):
    """
        Class for all tests about Partner Model
    """
    def test_c_partner(self):
        """
        Test Partner Model - Creation Test without image for tests
        """
        Client()
        partner = Partner.objects.create(name="Partner",
                                         description="Description",
                                         webSite="https://www.adapta-formation.com/")
        formatted_data = f"{partner.name} | {partner.description} | {partner.webSite}"
        expected_value = "Partner | Description | https://www.adapta-formation.com/"
        assert formatted_data == expected_value
