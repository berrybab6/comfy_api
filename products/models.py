from math import prod
from pyexpat import model
from statistics import mode
from turtle import width
from unicodedata import category
from django.db import models

# Create your models here.

class Products(models.Model):
    prod_title = models.CharField(max_length=255,null=False,blank=False)
    prod_description = models.CharField(max_length=255,null=True,blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    price_updated_at = models.DateTimeField(blank=True,null=True)
    price = models.DecimalField(max_digits=7, decimal_places=3)
    length = models.DecimalField(max_digits=5, decimal_places=3,null=True)
    height = models.DecimalField(max_digits=6, decimal_places=3,null=True)
    width = models.DecimalField(max_digits=7, decimal_places=3,null=True)
    prod_image = models.ImageField(upload_to = "products",null=True,blank=True)
    brand = models.CharField(max_length=150,blank=True,null=True)
    
    WOMENS = 1
    MENS = 2
    KIDS = 3

    CATEGORY_CHOICES = ((WOMENS, 'womens'), (MENS, 'mens'), (KIDS, 'kids'))
    ##dont Forget 
    prod_category = models.PositiveSmallIntegerField(
        choices=CATEGORY_CHOICES, null=True)
    # sizeColor = models.ManyToManyField('ItemSizeColor', related_name='products')




class ItemSizeColor(models.Model):
    XL = 1
    XXL = 2
    S = 3
    L = 4

    Size_CHOICES = ((XL, 'XL'), (XXL, 'XXL'), (S, 'S'),(L,'L'))
    ##dont Forget 
    size = models.PositiveSmallIntegerField(
        choices=Size_CHOICES, null=True)
    # item_size = models.ForeignKey(ItemSize, on_delete=models.CASCADE)

    RED = 1
    GREEN = 2
    WHITE = 3
    BLUE = 4
    SILVER = 5
    Color_CHOICES = ((RED, 'Red'), (GREEN, 'Green'), (WHITE, 'White'),(BLUE,'Blue'),(SILVER,'Silver'))
    color = models.PositiveSmallIntegerField(
        choices=Color_CHOICES, null=True)
    prod = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ("color", "size")

    # class Meta:
    #     db_table = 'item_colors'
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=('item_size', 'color'),
    #             name='unique_size_color'
    #         )
    #     ]

