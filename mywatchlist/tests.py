from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_html_url_exist(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml_url_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json_url_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
