from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, CustomUserViewSet, user_signup, user_login

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
# add CustomUserViewSet only if you really need it; otherwise omit to avoid dupes
# router.register(r"customusers", CustomUserViewSet, basename="customusers")

urlpatterns = [
    path("", include(router.urls)),
    path("signup/", user_signup, name="user_signup"),
    path("login/", user_login, name="login"),
    path("token/", obtain_auth_token, name="obtain-token"),  # DRF token endpoint
]
