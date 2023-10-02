from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('signup/', views.user_signup, name='user_signup'),
    path('api/auth/login/', obtain_auth_token, name='user_login'), 
]