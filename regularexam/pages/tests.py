from django.test import TestCase,SimpleTestCase
from django.urls import reverse


# Create your tests here.

class HomePageTest(SimpleTestCase):

    def test_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.status_code, 200)

    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

