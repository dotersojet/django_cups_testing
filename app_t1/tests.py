from django.test import TestCase
from django.test.client import Client,RequestFactory
from django.core.urlresolvers import reverse
from app_t1.views import contact_page
from app_t1.models import Contacts


# Create your tests here.

class Ticket1Test(TestCase):
    def setUp(self):
        """
        Set up initial data
        """  
        self.con = Contacts(name='kolian',skype='kolian1611')
        self.con.save()
    
    def test_contact_page(self):
        """
        Test our view response
        """
        resp = Client().get(reverse('contact_page'))
        self.assertContains(resp, 'kolian1611', status_code=200) 
 

class Ticket2Test(TestCase):
    """
    Test middleware which store requests
    """
    
    def test_request_middl(self):
        """
        Change remote_addr of client and look
        if result page contain such address
        """
        resp=Client().get(reverse('requests_page'), REMOTE_ADDR='9.9.9.9')
        self.assertContains(resp, '9.9.9.9', status_code=200)
        
        
        
        
        
        
