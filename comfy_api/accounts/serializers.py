from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class RegisterUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","username"]
class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ["email", "password"]