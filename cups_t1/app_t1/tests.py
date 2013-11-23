from django.test import TestCase
from django.http import HttpRequest
from app_t1.views import contact_page
# Create your tests here.
class Ticket1Test(TestCase):
    def test_contact_page(self):
        request=HttpRequest()
        resp=contact_page(request)
        self.assertEqual(resp.status_code,200)
        
