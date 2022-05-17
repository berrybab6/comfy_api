from account.serializers import UserSerializers
from .models import User
from rest_framework import serializers
from .models import ComfyProducts, ComfySale, Dimension, FavoriteProduct, ItemSizeColor, ProductImages,  ShippingInfo

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
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = "__all__"


    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            wished_item = ComfyProducts.objects.get(id=data['wished_item'])
            data['wished_item'] = ComfyProductsSerializer(wished_item).data

        except ComfyProducts.DoesNotExist:
            wished_item = None
        
        # try:
        #     user = User.objects.get(id=data['user_id'])
        #     data['user'] = UserSerializers(user).data
            
        # except User.DoesNotExist:
        #     user = None
        
        return data  
class FavoriteStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = ["status",]