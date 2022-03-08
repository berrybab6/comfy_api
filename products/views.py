from django.shortcuts import render
# from html5lib import serialize
from rest_framework import viewsets
from .models import Color, ItemSize, ItemSizeColor, Products
from .serializers import ColorSerializer, ColorSizeSerializer, ItemSizeSerializer, ProductSerializer
# Create your views here.

class ProductListView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        return super().get_queryset()

class ColorListView(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

    
    def get_queryset(self):
        return super().get_queryset()

class SizeListView(viewsets.ModelViewSet):
    serializer_class = ItemSizeSerializer
    queryset = ItemSize.objects.all()

    
    def get_queryset(self):
        return super().get_queryset()

class ItemSizeListView(viewsets.ModelViewSet):
    serializer_class = ColorSizeSerializer
    queryset = ItemSizeColor.objects.all()

    
    def get_queryset(self):
        return super().get_queryset()


