from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.TextField()
    phone  = models.IntegerField()
    message = models.TextField()
 
    
# def  __str__(self):

