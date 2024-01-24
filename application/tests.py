from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.

class TestSimple(TestCase):
    def test_semple_view(self):
        client = APIClient()
        response = client.get('/cicd/')
        self.assertEqual(response.status_code, second = 200)