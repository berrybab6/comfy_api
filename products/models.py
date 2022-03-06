from pyexpat import model
from statistics import mode
from turtle import width
from django.db import models

# Create your models here.
class Products(models.Model):
    prod_title = models.CharField(max_length=255,null=False,blank=False)
    prod_description = models.CharField(max_length=255,null=True,blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    price_updated_at = models.DateTimeField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=3)
    length = models.DecimalField(max_digits=5, decimal_places=3)
    height = models.DecimalField(max_digits=5, decimal_places=3)
    width = models.DecimalField(max_digits=3, decimal_places=3)
    brand = models.CharField(max_length=150,blank=True)
