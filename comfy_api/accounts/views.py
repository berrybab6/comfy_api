from importlib.metadata import requires
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
# from rest_framework.decorators import action
from .models import User
from rest_framework.response import Response
from .utils import Utils
from rest_framework.views import APIView


from django.contrib.auth.hashers import make_password,check_password

from .serializers import LoginSerializer, UserSerializers
# from rest_framework.authtoken.views import ObtainAuthToken

# , authenticate
from rest_framework.permissions import AllowAny
from rest_framework import generics, status, permissions
# from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
import random
import string
from rest_framework.authtoken.models import Token


# Create your views here.

class UserDetailView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny, ]

    def get(self, request,pk=None):
        try:

            if User.objects.filter(id=pk).exists():
                user = User.objects.get(id=pk)
                serialize = UserSerializers(user)
                return JsonResponse(serialize.data,safe=False, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"message":"No user Found with this id"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({"message":"No user Found "}, status=status.HTTP_404_NOT_FOUND)

class UserCreateView(generics.GenericAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny, ]


    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password", "")
        full_name = request.data.get("full_name", "")
        phone_number = request.data.get("phone_number","")
        email = request.data.get("email","")

        admin = request.data.get("admin",False)
        staff = request.data.get("staff",False)


        if email and username and password:
            if admin and staff:
                user = User.objects.create_superuser(username=username,
                                            email = email,
                                            password=password,
                                            full_name=full_name,
                                            phone_number = phone_number)
            else:
                user = User.objects.create_user(username=username,
                                            email = email,
                                            password=password,
                                            full_name=full_name,
                                            phone_number = phone_number)
           
            ser = UserSerializers(user)
            # return JsonResponse(ser.data, safe=False)

            return JsonResponse(ser.data,safe=False, status=status.HTTP_200_OK)
       
        else:
            return JsonResponse({"error":"Empty_field"})
    def get(self, request):
        if User.objects.all().exists():
            user = User.objects.all()

            serialize = UserSerializers(user,many=True)
            return JsonResponse(serialize.data,safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message":"No user Found with this id"}, status=status.HTTP_404_NOT_FOUND)

class LoginUserView(APIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = Utils.authenticate_sector_admin(serializer.validated_data)
        # queryset = user
        serializedUser = LoginSerializer(user)
        token = Utils.encode_token(user)
        
        return Response({"data":serializedUser.data, "token":token})
        
    def get_queryset(self):
        return super().get_queryset()
  