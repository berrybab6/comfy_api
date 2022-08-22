from datetime import datetime, timedelta
from math import prod
from django.shortcuts import render
# from requests import Response
# from html5lib import serialize
from rest_framework import viewsets
from .models import ComfyProducts, ComfySale, Dimension, FavoriteProduct, ItemSizeColor, ProductImages, ShippingInfo
from rest_framework import generics, permissions, status
from django.http import JsonResponse

from .serializers import ColorSizeSerializer, ComfyProductsAllSerializer, ComfyProductsSerializer, ComfyProductsTypeSerializer, ComfySaleSerializer, DimensionSerializer, FavoriteSerializer, FavoriteStatusSerializer, ImageCategorySerializer, ProductImagesSerializer, ShippingInfoSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ComfyProductView(viewsets.ModelViewSet):
    serializer_class = ComfyProductsAllSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return super().get_queryset()

class ProductsByTypeView(generics.GenericAPIView):
    serializer_class = ComfyProductsTypeSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get(self, request, category = None, itemType = None):
        try:
            if ComfyProducts.objects.filter(prod_category=category, item_type = itemType).exists():
                prod = ComfyProducts.objects.filter(prod_category=category, item_type = itemType)
                ser = ComfyProductsTypeSerializer(prod, many=True)
                return JsonResponse({"products":ser.data}, status = 200)
            else:
                return JsonResponse({"error":"No Products Found","products":[]},status=204)
        except:
            print("Helllloooo")
            return JsonResponse({"error":"Unable to fetch Products"}, status= 500)

    def get_queryset(self):
        return super().get_queryset()


class FeaturedProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsTypeSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        prod = ComfyProducts.objects.filter(featured =True)
        if prod:
            ser = ComfyProductsTypeSerializer(prod, many=True)
            return JsonResponse({"products":ser.data}, status= 200)
        else:
            JsonResponse({"error":"No Products Found"}, status=400)
    def get_queryset(self):
        return super().get_queryset()


class NewestProductsView(generics.GenericAPIView):
    serializer_class = ComfyProductsTypeSerializer
    queryset = ComfyProducts.objects.all()
    permission_classes = [IsAuthenticated, ]

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
    permission_classes = [IsAuthenticated, ]

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
    permission_classes = [IsAuthenticated, ]

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
    queryset = [ComfyProducts.objects.all(),Dimension.objects.all(),ProductImages.objects.all(), ItemSizeColor.objects.all(),]
    serializer_class = [ComfyProductsSerializer, ProductImagesSerializer, DimensionSerializer,ColorSizeSerializer,]
    permission_classes = [IsAuthenticated, ]

    def get(self, request,pk=None):
        # try:
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
from accounts.models import User
class FavoriteProductsView(generics.GenericAPIView):
    serializer_classes = [FavoriteProduct, ComfyProductsSerializer, FavoriteStatusSerializer]
    queryset = [FavoriteProduct.objects.all(),ComfyProducts.objects.all()]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        # user= User.objects.get(id=user_id)
        user = self.request.user

        try:

            if user:
                # user= User.objects.get(id=user_id)
                print("USR",user)
                favs = FavoriteProduct.objects.filter(user_id=user , status=True).order_by('-added_date')

                if favs:
                    ser = FavoriteSerializer(favs, many=True)
                    return JsonResponse({"products":ser.data})
                else:
                    return JsonResponse({"error":"No Fav item Found!!!","products":[]})
            else:
                return JsonResponse({"error":"No User Found with this id!!!"})
        except:
            return JsonResponse({"error":"No matching query!!!"}, status = 500)


    def post(self, request):
        try:
            user = self.request.user
            if user:
                print("LOLLLLL")
                prod_id=request.data.get("prod_id","")
                if prod_id !="":
                    if ComfyProducts.objects.filter(id=prod_id).exists():
                        # user= User.objects.get(id=user_id)
                        prod = ComfyProducts.objects.get(id=prod_id)
                        if(FavoriteProduct.objects.filter(user_id=user, wished_item=prod).exists()):
                            fav = FavoriteProduct.objects.get(user_id=user, wished_item=prod)
                            fav.status = not fav.status
                            fav.save()
                            # print("so here right")
                            ser = FavoriteStatusSerializer(fav)

                            return JsonResponse({"products":ser.data})
                        else:
                            fav = FavoriteProduct.objects.create(user_id=user, wished_item=prod)
                            fav.save()
                            ser = FavoriteStatusSerializer(fav)
                            return JsonResponse({"products":ser.data})
                    else:
                        return JsonResponse({"error":"No Product Found!!!"},status=204)
                return JsonResponse({"error":"Empty Field!!!"},status=400)
            else:
                return JsonResponse({"error":"No User item Found!!!"}, status=204)

        # favs = FavoriteProduct.objects.filter(user_id=user).order_by('-added_date')
        except:
            return JsonResponse({"error":"No matching query!!!"}, status = 500)
