from django.shortcuts import render
from html5lib import serialize
from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer
# Create your views here.

class ProductListView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        return super().get_queryset()
