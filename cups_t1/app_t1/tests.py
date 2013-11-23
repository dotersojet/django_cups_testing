from django.test import TestCase
from django.http import HttpRequest
from app_t1.views import contact_page
from app_t1.models import Contacts
# Create your tests here.
class Ticket1Test(TestCase):
    def test_contact_page(self):
        con=Contacts(name='kolian')
        con.save()
        request=HttpRequest()
        resp=contact_page(request)
        self.assertEqual(resp.status_code,200)
        
