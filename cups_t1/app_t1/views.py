from django.shortcuts import render,render_to_response
from app_t1.models import Contacts,Request
 
# Create your views here.

def contact_page(request):
    my_contact = Contacts.objects.get(name = 'kolian')
    return render_to_response('contact.html',{'my_contact':my_contact})

def requests_show(request):
    lst=Request.objects.order_by('-time')[:10]
    return render_to_response('requests.html',{'lst':lst})

