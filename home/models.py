from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
     return self.name

   
    
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to ='static/images/')
    categories = models.ManyToManyField(Category, related_name='products')
    
    def __str__(self):
     return self.name