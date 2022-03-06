import requests

from django.test import TestCase

class UrlTestCase(TestCase):
    def setUp(self):
        self.url = 'https://www.digikala.com/search/?q=%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C'

    def test_url_is_valid(self):
        status = requests.get(self.url)
        self.assertEqual(status.status_code,200)