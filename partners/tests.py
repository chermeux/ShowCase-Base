# pylint: disable=E1101
"""
    Tests file about partners app - 3 parts (Import, Views Tests, Models Tests)
    It's in oder CRUD
"""
############################ Import, Librairies etc ##############################

from django.test import TestCase, Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from partners.models import Partner
from partners.forms import PartnerForm


############################ Tests Views about Partner ##############################
class CreateTestCasePartner(TestCase):
    """
        Class for all tests about Create Partner
    """
    def test_get_request_renders_create_partner_template(self):
        """
        Test that the view renders the 'Partners/CreatePartner.html' template for a GET request
        """
        url = reverse('Partner_c')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Partners/CreatePartner.html')
        self.assertIsInstance(response.context['form'], PartnerForm)

    def test_post_request_with_invalid_data_shows_form_errors(self):
        """
        Test that the view shows form errors for an invalid POST request
        """
        url = reverse('Partner_c')
        # Empty data, which should make the form invalid
        data = {}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Partners/CreatePartner.html')
        self.assertIsInstance(response.context['form'], PartnerForm)
        #self.assertContains(response, "This field is required.")  # Check for the error message

        # Check that no new Partner instance was created in the database
        partners_count = Partner.objects.count()
        self.assertEqual(partners_count, 0)


class ReadTestCasePartner(TestCase):
    """
        Class for all tests about Read Partner (page to display partners...)
    """
    def test_r_partners(self):
        """
        Test Partners Page - HTML PartnersMain - status_code=200 and good template
        """
        client = Client()
        response = client.get("/partners/")
        self.assertEqual(response.status_code, 200)
        assertTemplateUsed(response, "Partners/PartnersMain.html")


class UpdateTestCasePartner(TestCase):
    """
        Class for all tests about Update Partner
    """
    def setUp(self):
        """
        Create a Partner instance to use in the tests
        """
        self.partner = Partner.objects.create(
            name="Test Partner",
            description="Test Description",
            webSite="https://example.com",
            logo="test_logo.png",
        )

    def test_get_request(self):
        """
        Test the view with a GET request
        """
        url = reverse('Partner_u', args=[self.partner.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PartnerForm)  #correct form used in template


    def test_post_valid_form(self):
        """
        Test the view with a POST request with valid data
        """
        url = reverse('Partner_u', args=[self.partner.id])
        data = {
            'name': 'Updated Partner Name',
            'description': 'Updated Description',
            'webSite': 'https://updated.com',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


        # Check if the data was updated in the database
        updated_partner = Partner.objects.get(id=self.partner.id)
        self.assertEqual(updated_partner.name, 'Updated Partner Name')
        self.assertEqual(updated_partner.description, 'Updated Description')
        self.assertEqual(updated_partner.webSite, 'https://updated.com')

    def test_post_invalid_form(self):
        """
        Test the view with a POST request with invalid data
        """
        url = reverse('Partner_u', args=[self.partner.id])
        data = {}  # Empty data, which should make the form invalid
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PartnerForm) #correct form used in template

        # Check if the data in the database remains unchanged
        unchanged_partner = Partner.objects.get(id=self.partner.id)
        self.assertEqual(unchanged_partner.name, 'Test Partner')
        self.assertEqual(unchanged_partner.description, 'Test Description')
        self.assertEqual(unchanged_partner.webSite, 'https://example.com')
        self.assertEqual(unchanged_partner.logo, 'test_logo.png')

class DeleteTestCasePartner(TestCase):
    """
        Class for all tests about Delete Partner
    """
    def setUp(self):
        """
        Create a Partner instance to use in the tests
        """
        self.partner = Partner.objects.create(
            name="Test Partner",
            description="Test Description",
            webSite="https://example.com",
            logo="test_logo.png",
        )

    def test_post_request_deletes_partner(self):
        """
         Test if the view delete correctly the partner when a Post request is done
        """
        url = reverse('Partner_d', args=[self.partner.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/partners/')

        with self.assertRaises(Partner.DoesNotExist):
            Partner.objects.get(id=self.partner.id)

    def test_get_request_renders_confirm_delete_template(self):
        """
        Test view correctly in 'base/confirmDelete.html' when a GET request is made
        """
        url = reverse('Partner_d', args=[self.partner.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/confirmDelete.html')


############################### Tests Partner Model ################################
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
