from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    con_name = models.CharField(max_length=255)
    con_email = models.EmailField()
    con_subject = models.CharField(max_length=255)
    con_message = models.TextField()
    
class signup(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)    
    email = models.EmailField()


