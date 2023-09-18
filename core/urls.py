from django.urls import path
from . import views


urlpatterns = [
    # Add URL patterns for your Django views here
     path('api/homepage/', views.get_homepage_data, name='get_homepage_data'),
]

