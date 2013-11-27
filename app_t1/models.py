from django.db import models

# Create your models here.
class Contacts(models.Model): 
    """
    Model class which contain fields of 
    information on the main page
    """
    name=models.CharField(max_length=20, blank=True, null=True)
    last_name=models.CharField(max_length=20, blank=True, null=True)
    date_of_birth=models.DateField(blank=True, null=True)
    bio=models.TextField(blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    jabber=models.CharField(max_length=20, blank=True, null=True)
    skype=models.CharField(max_length=20, blank=True, null=True)
    other_contacts=models.TextField(blank=True, null=True) 


class Requests(models.Model):
    """
    Model class that store information about
    user requests from middleware
    """
    name = models.CharField(max_length=20, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        """
        Order info in Requests tables
        by time
        """
        ordering = ['-time']
        
