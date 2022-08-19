from email.policy import default
from math import prod
from pyexpat import model
from statistics import mode
from turtle import width
from unicodedata import category
from django.db import models
from accounts.models import User
from django.conf import settings

# Create your models here.
class ComfyProducts(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True,null=True)
    # status = models.CharField(default="publish", max_length=100)
    featured = models.BooleanField(default=False)
    catalog_visiblity = models.CharField(default="visible",max_length=100)
    description = models.CharField(max_length=340,blank=True,null=True)
    short_description = models.CharField(max_length=255,blank=True,null=True)
    image_url = models.ImageField(upload_to = "products",null=True, blank=True)


    price = models.DecimalField(max_digits=7, decimal_places=3)
    regular_price = models.DecimalField(max_digits=7, decimal_places=2,null=True)

    WOMENS = 1
    MENS = 2
    KIDS = 3

    CATEGORY_CHOICES = ((WOMENS, 'womens'), (MENS, 'mens'), (KIDS, 'kids'))
   
        ##########for Women
    DRESS = "dress"
    JUMPSUIT = "jumpsuit"
    TWO_PIECE_CLOTHES = "two_piece_clothes"
    WOMEN_SUIT = "women_suit"
    PAJAMAS = "pajamas"
    WOMEN_BLAZER = "women_blazer"
    TOP = "top"
    SKIRT = "skirt"
    ACCESORY = "accesory"
    BAG = "bag"
    WOMEN_TROUSER= "women_trouser"
    ###### for Boys
    T_SHIRT = "t_shirt"
    TROUSER = "trouser"
    WATCH = "watch"
    
    ###For Baby
    TOYS = "toys"
    KIDS_BAG = "kids_bag"
 
    ITEM_TYPE = (
    ##########for Women
    (DRESS, "dress"),
    (JUMPSUIT , "jumpsuit"),
    (TWO_PIECE_CLOTHES ,"two_piece_clothes"),
    (WOMEN_SUIT , "women_suit"),
    (PAJAMAS , "pajamas"),
    (WOMEN_BLAZER , "women_blazer"),
    (TOP , "top"),
    (SKIRT ,"skirt"),
    (ACCESORY , "accesory"),
    (BAG ,"bag"),
    (WOMEN_TROUSER , "women_trouser"),
    ###### for Boys
    (T_SHIRT , "t_shirt"),
    (TROUSER , "trouser"),
    (WATCH , "watch"),
     ###For Baby
    (TOYS , "toys"),
    (KIDS_BAG , "kids_bag"),
         )       
    item_type = models.CharField(
        choices=ITEM_TYPE, max_length=50,null=True)
    prod_category = models.PositiveSmallIntegerField(
        choices=CATEGORY_CHOICES, null=True)
    brand = models.CharField(max_length=100,null=True, blank=True)

    

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


class FavoriteProduct(models.Model):
    wished_item = models.ForeignKey(ComfyProducts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ["wished_item", "user_id"]
        db_table = 'favorite'