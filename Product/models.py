from django.db import models
from Categories.models import Categories 
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    categories  = models.ForeignKey(Categories,  on_delete=models.CASCADE)
    
class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    
    
    def __str__(self)  -> str:
        return self.name 
    