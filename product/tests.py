# pylint: disable=E1101
"""
    Tests file about product app - 3 parts (Import, Views Tests, Models Tests)
    It's in oder CRUD
"""
############################ Import, Librairies etc ##############################

from django.test import TestCase, Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from product.models import Product, Category
from product.forms import ProductForm


############################ Tests Views about Product App ##############################

##### Tests Product Views #####
class CreateTestCaseProduct(TestCase):
    """
        Class for all tests about Create Product
    """
    def test_get_request_renders_create_product_template(self):
        """
        Test that the view renders the 'Product/CreateProduct.html' template for a GET request
        """
        url = reverse('Product_c')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Product/CreateProduct.html')
        self.assertIsInstance(response.context['form'], ProductForm)

    def test_post_request_with_invalid_data_shows_form_errors(self):
        """
        Test that the view shows form errors for an invalid POST request
        """
        url = reverse('Product_c')
        # Empty data, which should make the form invalid
        data = {}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Product/CreateProduct.html')
        self.assertIsInstance(response.context['form'], ProductForm)
        #self.assertContains(response, "This field is required.")  # Check for the error message

        # Check that no new Product instance was created in the database
        products_count = Product.objects.count()
        self.assertEqual(products_count, 0)


class ReadTestCaseProduct(TestCase):
    """
        Class for all tests about Read Product (page to display products...)
    """
    def test_r_products(self):
        """
        Test Products Page - HTML ProductsMain - status_code=200 and good template
        """
        client = Client()
        response = client.get("/product/")
        self.assertEqual(response.status_code, 200)
        assertTemplateUsed(response, "Product/ProductsMain.html")


class UpdateTestCaseProduct(TestCase):
    """
        Class for all tests about Update Product
    """
    def setUp(self):
        """
        Create a Product instance to use in the tests
        """
        self.product = Product.objects.create(
            title="Test Product",
            description="Test Description",
            image="image_test.png",
        )

    def test_get_request(self):
        """
        Test the view with a GET request
        """
        url = reverse('Product_u', args=[self.product.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProductForm)  #correct form used in template


    def test_post_valid_form(self):
        """
        Test the view with a POST request with valid data
        """
        url = reverse('Product_u', args=[self.product.id])
        data = {
            'title': 'Updated Product Title',
            'description': 'Updated Description',
            'image': "updated_image_test.png",

        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


        # Check if the data was updated in the database
        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.title, 'Updated Product Title')
        self.assertEqual(updated_product.description, 'Updated Description')

    def test_post_invalid_form(self):
        """
        Test the view with a POST request with invalid data
        """
        url = reverse('Product_u', args=[self.product.id])
        data = {}  # Empty data, which should make the form invalid
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ProductForm) #correct form used in template

        # Check if the data in the database remains unchanged
        unchanged_product = Product.objects.get(id=self.product.id)
        self.assertEqual(unchanged_product.title, 'Test Product')
        self.assertEqual(unchanged_product.description, 'Test Description')
        self.assertEqual(unchanged_product.image, 'image_test.png')


class DeleteTestCaseProduct(TestCase):
    """
        Class for all tests about Delete Product
    """
    def setUp(self):
        """
        Create a Product instance to use in the tests
        """
        self.product = Product.objects.create(
            title="Test Product",
            description="Test Description",
        )

    def test_post_request_deletes_product(self):
        """
         Test if the view delete correctly the product when a Post request is done
        """
        url = reverse('Product_d', args=[self.product.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/product/')

        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product.id)

    def test_get_request_renders_confirm_delete_template(self):
        """
        Test view correctly in 'base/confirmDelete.html' when a GET request is made
        """
        url = reverse('Product_d', args=[self.product.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/confirmDelete.html')

##### Tests Category Views #####
#it's same that product

############################### Tests Product Model ################################
class ModelTestCaseProduct(TestCase):
    """
        Class for all tests about Product Model
    """
    def test_c_product(self):
        """
        Test Product Model - Creation Test without image for tests
        """
        Client()
        product = Product.objects.create(title="Product",
                                         description="Description")
        formatted_data = f"{product.title} | {product.description}"
        expected_value = "Product | Description"
        assert formatted_data == expected_value

class ModelTestCaseCategory(TestCase):
    """
        Class for all tests about Category Model
    """
    def test_c_product(self):
        """
        Test Category Model - Creation Test without image for tests
        """
        Client()
        category = Category.objects.create(name="Category",
                                         description="Description")
        formatted_data = f"{category.name} | {category.description}"
        expected_value = "Category | Description"
        assert formatted_data == expected_value
