from email.policy import default
from math import prod
from pyexpat import model
from statistics import mode
from turtle import width
from unicodedata import category
from django.db import models

# Create your models here.
class ComfyProducts(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_created_gmt = models.DateTimeField(null=True,blank=True)
    date_modified = models.DateTimeField(blank=True,null=True)
    date_modified_gmt = models.DateTimeField(blank=True,null=True)
    name = models.CharField(max_length=255,null=False,blank=False, default="simple")
    status = models.CharField(default="publish", max_length=100)
    featured = models.BooleanField(default=False)
    catalog_visiblity = models.CharField(default="visible",max_length=100)
    description = models.CharField(max_length=340,blank=True,null=True)
    short_description = models.CharField(max_length=255,blank=True,null=True)
    sku = models.CharField(max_length=100, default="wp_pennant")

    price = models.DecimalField(max_digits=7, decimal_places=3)
    regular_price = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    price = models.DecimalField(max_digits=7, decimal_places=3)

    WOMENS = 1
    MENS = 2
    KIDS = 3

    CATEGORY_CHOICES = ((WOMENS, 'womens'), (MENS, 'mens'), (KIDS, 'kids'))
      
     
    prod_category = models.PositiveSmallIntegerField(
        choices=CATEGORY_CHOICES, null=True)
    brand = models.CharField(max_length=100,null=True, blank=True)

    # sale_price = models.DecimalField(max_digits=5, decimal_places=3,null=True)

    def __str__(self):
        return  self.name

class ComfySale(models.Model):
    comfy_product = models.OneToOneField(
        ComfyProducts,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    sale_price = models.DecimalField(max_digits=7,decimal_places=2)
    date_on_sale_from = models.DateTimeField(null=True)
    date_on_sale_from_gmt= models.DateTimeField(null=True)
    date_on_sale_to = models.DateTimeField(null=True)
    date_on_sale_to_gmt = models.DateTimeField(null=True)
    on_sale = models.BooleanField(default=False)
    purchasable = models.BooleanField(default=True)

    def __str__(self):
        return  self.comfy_product.name

class Dimension(models.Model):
    comfy_product = models.OneToOneField(
        ComfyProducts,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    height = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.comfy_product.name

class ShippingInfo(models.Model):
    comfy_product = models.OneToOneField(
        ComfyProducts,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    shipping_required = models.BooleanField(default=False,null=True)
    shipping_taxable = models.BooleanField(default=False,null=True)


    def __str__(self):
        return self.comfy_product.name
class ProductImages(models.Model):
    comfy_product = models.ForeignKey(ComfyProducts,on_delete=models.CASCADE)
    src = models.ImageField(upload_to = "products",null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank= True)


    def __str__(self):
        return  self.comfy_product.name

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


# 
    # def __str__(self):
        # return "%s the Product" % self.comfy_product.name

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
    prod = models.ForeignKey(ComfyProducts,on_delete=models.CASCADE)
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

