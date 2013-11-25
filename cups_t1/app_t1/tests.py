from django.test import TestCase
from django.http import HttpRequest
from app_t1.views import contact_page
from app_t1.models import Contacts, Request
from app_t1.middleware import RequestCounting
from django.test.client import RequestFactory

# Create your tests here.

class Ticket1Test(TestCase):

    def test_contact_page(self):
        con = Contacts(name = 'kolian',skype = 'kolian1611')
        con.save()
        request = HttpRequest()
        resp = contact_page(request)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.content.find('kolian1623') > 0)
        self.assertTrue(resp.content.find('kolian1611') > 0)
        
        
class MiddlewareTest(TestCase):

    def setUp(self):
        self.md = RequestCounting()
        self.request = HttpRequest()
        self.request.META['REMOTE_ADDR'] = '1.1.1.1'
        self.request.session = {}
        
    def test_middleware(self):
        self.assertEqual(self.md.process_request(self.request), None)
        test_addr = Request.objects.get(name = '1.1.1.1')
        self.assertEqual(test_addr.name, '1.1.1.1')
        
        
class ContextProcessorsTest(TestCase):

    def test_context_proc(self):
        from django.conf import settings
        from django.template import RequestContext        
        factory = RequestFactory()
        request = factory.get('/')
        c = RequestContext(request)
        self.assertTrue('settings' in c)
        self.assertTrue('BASE_DIR' in c['settings'])
        self.assertEqual(c['settings']['BASE_DIR'], settings.BASE_DIR)
        

