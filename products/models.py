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
    # sizeColor = models.ManyToManyField('SizeColor', related_name='products')


class Color(models.Model):
    color = models.CharField(max_length=128)

class ItemSize(models.Model):
    size = models.CharField(max_length=128)
    colors = models.ManyToManyField(
        Color,
        related_name='item_sizes',
        through='ItemSizeColor'
    )
class ItemSizeColor(models.Model):
    item_size = models.ForeignKey(ItemSize, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'item_colors'
        constraints = [
            models.UniqueConstraint(
                fields=('item_size', 'color'),
                name='unique_size_color'
            )
        ]