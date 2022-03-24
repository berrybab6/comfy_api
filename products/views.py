from datetime import datetime, timedelta
from django.shortcuts import render
# from html5lib import serialize
from rest_framework import viewsets
from .models import ComfyProducts, ComfySale, Dimension, ItemSizeColor, ProductImages, Products, ShippingInfo
from rest_framework import generics, permissions, status
from django.http import JsonResponse

from .serializers import ColorSizeSerializer, ComfyProductsSerializer, ComfySaleSerializer, DimensionSerializer, ProductImagesSerializer, ProductSerializer, ShippingInfoSerializer
# Create your views here.

class ProductListView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        return super().get_queryset()

class ComfyProductView(viewsets.ModelViewSet):
    serializer_class = ComfyProductsSerializer
    queryset = ComfyProducts.objects.all()

    
    def get_queryset(self):
        return super().get_queryset()

class FeaturedProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        prod = ComfyProducts.objects.filter(featured =True)
        if prod:
            ser = ComfyProductsSerializer(prod, many=True)
            return JsonResponse({"products":ser.data})
        else:
            JsonResponse({"error":"No Products Found"})
    def get_queryset(self):
        return super().get_queryset()

class NewestProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        zare = datetime.today()
        
            
        d = datetime.today() - timedelta(days=7)

        prod = ComfyProducts.objects.filter(date_created__range=[d, zare])
        if prod:
            ser = ComfyProductsSerializer(prod, many=True)
            return JsonResponse({"products":ser.data})
        else:
            return JsonResponse({"error":"No Products Found"})
    def get_queryset(self):
        return super().get_queryset()


class CategoryProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request,category=None):
        prod = ComfyProducts.objects.filter(prod_category=category)
        if prod:
            ser = ComfyProductsSerializer(prod, many=True)
            return JsonResponse({"products":ser.data})
        else:
            return JsonResponse({"error":"No Products Found"})
    def get_queryset(self):
        return super().get_queryset()

class ComfySaleView(viewsets.ModelViewSet):
    serializer_class = ComfySaleSerializer
    queryset = ComfySale.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()

class DimensionView(viewsets.ModelViewSet):
    serializer_class = DimensionSerializer
    queryset = Dimension.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()

class ShippingInfoView(viewsets.ModelViewSet):
    serializer_class = ShippingInfoSerializer
    queryset = ShippingInfo.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()

class ProductImagesView(viewsets.ModelViewSet):
    serializer_class = ProductImagesSerializer
    queryset = ProductImages.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()

class ItemSizeListView(viewsets.ModelViewSet):
    serializer_class = ColorSizeSerializer
    queryset = ItemSizeColor.objects.all()

    
    def get_queryset(self):
        return super().get_queryset()


# class ProductsDetailView(generics.GenericAPIView):


    
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
