from django.shortcuts import render
# from html5lib import serialize
from rest_framework import viewsets
from .models import ItemSizeColor, Products
from rest_framework import generics, permissions, status
from django.http import JsonResponse

from .serializers import ColorSizeSerializer, ProductSerializer
# Create your views here.

class ProductListView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        return super().get_queryset()

class ItemSizeListView(viewsets.ModelViewSet):
    serializer_class = ColorSizeSerializer
    queryset = ItemSizeColor.objects.all()

    
    def get_queryset(self):
        return super().get_queryset()
class ProductsDetailView(generics.GenericAPIView):
    queryset = [ItemSizeColor.objects.all(),Products.objects.all()]
    

    serializer_class = [ProductSerializer,ColorSizeSerializer,]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request,pk=None):
        product = Products.objects.get(id=pk)
        if product:
            item = ItemSizeColor.objects.get(prod=product)
            if item:
                ser = ColorSizeSerializer(item)
                ser2 = ProductSerializer(product)
                return JsonResponse({"product":ser2.data,"item_color":ser.data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error":"There is no other detail with this prodID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({"error":"Product Doesnot exist"}, status=status.HTTP_404_NOT_FOUND)

    # def get_queryset(self):
    #     return super().get_queryset()
