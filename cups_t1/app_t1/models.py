from django.db import models

# Create your models here.
class Contacts(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length = 20, blank = True, null = True)
    last_name = models.CharField(max_length = 20, blank = True, null = True)
    date_of_birth = models.DateField(blank = True, null = True)
    bio = models.TextField(blank = True, null = True)
    last_name = models.CharField(max_length = 20, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    jabber = models.CharField(max_length = 20, blank = True, null = True)
    skype = models.CharField(max_length = 20, blank = True, null = True)
    other_contacts = models.TextField(blank = True, null = True)
=======
    name=models.CharField(max_length=20,blank=True,null=True)
    last_name=models.CharField(max_length=20,blank=True,null=True)
    date_of_birth=models.DateField(blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    last_name=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    jabber=models.CharField(max_length=20,blank=True,null=True)
    skype=models.CharField(max_length=20,blank=True,null=True)
    other_contacts=models.TextField(blank=True,null=True)
    
class Request(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    time=models.DateTimeField(blank=True,null=True)
>>>>>>> ab725a13a76ed843f89f3bc252d34496071d136b
