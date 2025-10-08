from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","date_joined")

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ("username","email","password")
    def create(self, data):
        return User.objects.create_user(
            username=data["username"],
            email=data.get("email",""),
            password=data["password"],
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
