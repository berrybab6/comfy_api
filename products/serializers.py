from pyexpat import model
from rest_framework import serializers
from .models import ItemSizeColor, Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class ColorSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSizeColor
        fields = "__all__"
