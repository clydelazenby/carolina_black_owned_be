from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

from .serializers import (
    RegisterSerializer, LoginSerializer, CustomUserSerializer
)
from .models import CustomUser

User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def user_signup(request):
    s = RegisterSerializer(data=request.data)
    if not s.is_valid():
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    user = s.save()
    token, _ = Token.objects.get_or_create(user=user)
    return Response(
        {"status":"success","message":"User created","token": token.key},
        status=status.HTTP_201_CREATED
    )

@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    s = LoginSerializer(data=request.data)
    if not s.is_valid():
        return Response({"message":"Invalid data","errors": s.errors},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(
        request,
        username=s.validated_data["username"],
        password=s.validated_data["password"],
    )
    if not user:
        return Response({"message":"Invalid username or password"},
                        status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"status":"success","token": token.key}, status=status.HTTP_200_OK)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = CustomUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
