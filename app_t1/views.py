from django.shortcuts import render,render_to_response
from app_t1.models import Contacts,Requests
 
# Create your views here.

def contact_page(request):
    """
    Show user information on the main page
    """
    my_contact = Contacts.objects.all()[0]
    return render_to_response('contact.html',{'my_contact':my_contact})
    
def requests_page(request):
    """
    Show 10 ast requests from database
    """
    request_list=Requests.objects.all()[:10]
    return render_to_response('requests_page.html', {'list':request_list})
 
