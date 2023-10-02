from django.contrib.auth.backends import BaseBackend
from .models import CustomUser  # Import your CustomUser model

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None  # User not found

        if user.check_password(password):
            return user  # Authentication successful

        return None  # Incorrect password

    # Optionally, implement the `get_user` method to retrieve a user by ID.
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
