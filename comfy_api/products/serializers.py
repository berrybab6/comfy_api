from rest_framework import serializers
from .models import ComfyProducts, ComfySale, Dimension, ItemSizeColor, ProductImages,  ShippingInfo

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = "__all__"

class ColorSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSizeColor
        fields = "__all__"

class ImageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComfyProducts
        fields = ['image_url']

class ComfyProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComfyProducts
        fields = "__all__"

class ComfyProductsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComfyProducts
        fields = ["id","name", "price", "regular_price", "item_type", "prod_category", "image_url"]

class ComfyProductsAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComfyProducts
        fields = "__all__"

class ComfySaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComfySale
        fields = "__all__"
class DimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        fields = "__all__"
        

class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInfo
        fields = "__all__"

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"
        