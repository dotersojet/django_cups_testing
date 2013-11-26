from django.test import TestCase
from django.test.client import Client,RequestFactory
from django.core.urlresolvers import resolve
from app_t1.views import contact_page
from app_t1.models import Contacts


# Create your tests here.

class Ticket1Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.con = Contacts(name = 'kolian',skype = 'kolian1611')
        self.con.save()
        
    def test_contact_page(self):
        found=resolve('/')
        resp=self.client.get('/')   
        self.assertEqual(found.func,contact_page) 
        self.assertContains(resp,'kolian1611',status_code=200) 
