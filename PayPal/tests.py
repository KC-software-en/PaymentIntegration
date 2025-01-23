from django.test import TestCase

# RequestFactory returns a request
from django.test.client import RequestFactory

# import the views to be tested
from .views import *

#############################################################################################

# Create your tests here.

# Test for the index view.
class TestIndexView(TestCase):
    # Create a setUp method to create a user which is logged in before each test.
    def setUp(self):
        # Create a RequestFactory instance.
        self.factory = RequestFactory()        

    def test_index_status(self):
        # Make a request to the '/payment/' endpoint.
        request = self.factory.get('/payment/')

        # call the index view with a mock request response
        response = index(request)

        # Assert that the response is ok
        self.assertEqual(response.status_code, 200)
