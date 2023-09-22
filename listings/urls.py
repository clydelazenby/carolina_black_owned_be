from django.urls import path
from . import views

urlpatterns = [
    path('api/listings/', views.list_listings, name='list-listings'),
    path('api/listings/add/', views.add_listing, name='add-listing'),
    path('api/listings/update/<int:listing_id>/', views.update_listing, name='update-listing'),
    path('api/listings/delete/<int:listing_id>/', views.delete_listing, name='delete-listing'),
]