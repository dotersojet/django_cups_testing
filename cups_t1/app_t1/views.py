from django.shortcuts import render,render_to_response
from app_t1.models import Contacts
# Create your views here.

def contact_page(request):
    my_contact = Contacts.objects.get(name = 'kolian')
    return render_to_response('contact.html',{'my_contact':my_contact})
