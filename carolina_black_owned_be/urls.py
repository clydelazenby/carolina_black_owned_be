"""
URL configuration for carolina_black_owned_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from core import views as core_views
from auth_app import views as auth_views  # Import your auth_app views here
from django.conf import settings
from django.conf.urls.static import static
from listings import views
from django.http import JsonResponse




urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', auth_views.user_signup, name='user_signup'),
    path('api/auth/login/', auth_views.user_login, name='user_login'),
    # path('register/', auth_views.RegisterUserView.as_view(), name='register_user'),
    path('api/listings/', views.list_listings, name='list-listings'),
    path('api/listings/add/', views.add_listing, name='add-listing'),
    path('api/listings/update/<int:listing_id>/', views.update_listing, name='update-listing'),
    path('api/listings/delete/<int:listing_id>/', views.delete_listing, name='delete-listing'),
    path('api/debug/', lambda request: JsonResponse({'message': 'Debugging route'})),
    path('api/signup/', auth_views.user_signup, name='user_signup'),  # Use auth_views
    path('api/homepage/', core_views.get_homepage_data, name='homepage'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
