from datetime import datetime, timedelta
from math import prod
from django.shortcuts import render
# from html5lib import serialize
from rest_framework import viewsets
from .models import ComfyProducts, ComfySale, Dimension, FavoriteProduct, ItemSizeColor, ProductImages, ShippingInfo
from rest_framework import generics, permissions, status
from django.http import JsonResponse

from .serializers import ColorSizeSerializer, ComfyProductsAllSerializer, ComfyProductsSerializer, ComfyProductsTypeSerializer, ComfySaleSerializer, DimensionSerializer, FavoriteSerializer, ImageCategorySerializer, ProductImagesSerializer, ShippingInfoSerializer
# Create your views here.


class ComfyProductView(viewsets.ModelViewSet):
    serializer_class = ComfyProductsAllSerializer
    queryset = ComfyProducts.objects.all()

    
    def get_queryset(self):
        return super().get_queryset()

class ProductsByTypeView(generics.GenericAPIView):
    serializer_class = ComfyProductsTypeSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, category = None, itemType = None):
        prod = ComfyProducts.objects.filter(prod_category=category, item_type = itemType)
        if prod:
            ser = ComfyProductsTypeSerializer(prod, many=True)
            return JsonResponse({"products":ser.data})
        else:
            JsonResponse({"error":"No Products Found"})
    def get_queryset(self):
        return super().get_queryset()


class FeaturedProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsTypeSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        prod = ComfyProducts.objects.filter(featured =True)
        if prod:
            ser = ComfyProductsTypeSerializer(prod, many=True)
            return JsonResponse({"products":ser.data})
        else:
            JsonResponse({"error":"No Products Found"})
    def get_queryset(self):
        return super().get_queryset()


class NewestProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsTypeSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        zare = datetime.today()
        
            
        d = datetime.today() - timedelta(days=7)

        prod = ComfyProducts.objects.filter(date_created__range=[d, zare])
        if prod:
            ser = ComfyProductsTypeSerializer(prod, many=True)
            return JsonResponse({"products":ser.data})
        else:
            return JsonResponse({"error":"No Products Found"})
    def get_queryset(self):
        return super().get_queryset()


class ImageCategoryProductsView(generics.GenericAPIView):
    serializer_class = ImageCategorySerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request,category=None):

        images = ComfyProducts.objects.filter(prod_category=category).order_by('?')[:6]

        if images:
            ser = ImageCategorySerializer(images, many=True)
            return JsonResponse({"images":ser.data})
        else:
            return JsonResponse({"error":"No Image Found!!!"})

class CategoryProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsTypeSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get(self, request,category=None):
        # featured = ComfyProducts.objects.filter(prod_category=category)
        
        prod = ComfyProducts.objects.filter(prod_category=category)
        if prod :
            # ser = ComfyProductsSerializer(featured, many=True)
            ser2 = ComfyProductsTypeSerializer(prod, many=True)

            return JsonResponse({"products":ser2.data})
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


class ComfyProductsDetailView(generics.GenericAPIView):
    queryset = [ComfyProducts.objects.all(),Dimension.objects.all(),ProductImages.objects.all(), ItemSizeColor.objects.all()]
    

    serializer_class = [ComfyProductsSerializer, ProductImagesSerializer, DimensionSerializer,ColorSizeSerializer]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request,pk=None):
        product = ComfyProducts.objects.get(id=pk)
        if product:
            item = ItemSizeColor.objects.filter(prod=product)
            images = ProductImages.objects.filter(comfy_product=product)
            dimension = Dimension.objects.filter(comfy_product=product)
            # if images :
            ser = ColorSizeSerializer(item, many=True)
            ser3 = DimensionSerializer(dimension,many=True)
            ser4 = ProductImagesSerializer(images, many=True)
            ser2 = ComfyProductsSerializer(product)
            return JsonResponse({"product":ser2.data, "item":ser.data,"dimension":ser3.data, "Images":ser4.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"error":"There is no other detail with this prodID"}, status=status.HTTP_404_NOT_FOUND)
        # else:
            # return JsonResponse({"error":"Product Doesnot exist"}, status=status.HTTP_404_NOT_FOUND)



    def get_queryset(self):
        return super().get_queryset()


##################Favorite
from account.models import User
class FavoriteProductsView(generics.GenericAPIView):
    serializer_class = [FavoriteProduct, ComfyProductsSerializer]
    queryset = [FavoriteProduct.objects.all(),ComfyProducts.objects.all()]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request,user_id=None):
        user= User.objects.get(id=user_id)
        if user:
            favs = FavoriteProduct.objects.filter(user_id=user).order_by('-added_date')

            if favs:
                ser = FavoriteSerializer(favs, many=True)
                return JsonResponse({"products":ser.data})
            else:
                return JsonResponse({"error":"No Fav item Found!!!"})
        else:
            return JsonResponse({"error":"No User Found with this id!!!"})

    def post(self, request,user_id=None, prod_id=None):
        user= User.objects.get(id=user_id)
        prod = ComfyProducts.objects.get(id=prod_id)
        if user and prod:
            fav = FavoriteProduct.objects.create(user_id=user, wished_item=prod_id)
            fav.save()
            ser = FavoriteSerializer(fav)
            return JsonResponse({"products":ser.data})

        else:
            return JsonResponse({"error":"No User item Found!!!"})

        favs = FavoriteProduct.objects.filter(user_id=user).order_by('-added_date')
