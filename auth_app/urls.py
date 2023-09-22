from django.urls import path, include 
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter
# from listings import views
from . import views

# Create a router for user-related views (optional)
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('api/listings/', include('listings.urls')),
    
    path('signup/', views.user_signup, name='user_signup'),
    path('api/auth/login/', views.user_login, name='user_login'),
    # path('register/', views.RegisterUserView.as_view(), name='register_user'),
    # Add other URL patterns for your user-related views here
]
