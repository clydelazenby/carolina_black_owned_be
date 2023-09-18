# auth_app/serializers.py

from rest_framework import serializers
from .models import CustomUser  # Import your User model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # You can customize this based on your needs
