from pyexpat import model
from rest_framework import serializers
from .models import ItemSizeColor, Products,Color,ItemSize

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
class ItemSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSize
        fields = "__all__"
class ColorSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSizeColor
        fields = "__all__"