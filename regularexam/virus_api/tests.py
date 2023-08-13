from django.test import TestCase
from .models import ScanningLink
# Create your tests here.

class ScannedLinkTest(TestCase):

    def test_url_field(self):
        link = ScanningLink.objects.create(
            url='https://www.google.com'
        )
        self.assertEqual(link.url,'https://www.google.com')