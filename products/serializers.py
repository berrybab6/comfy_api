from pyexpat import model
from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializers):
    class Meta:
        model = Products
        fields = "__all__"