from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.list_listings, name='list-listings'),
    path('listings/add/', views.add_listing, name='add-listing'),
    path('listings/update/<int:listing_id>/', views.update_listing, name='update-listing'),
    path('listings/delete/<int:listing_id>/', views.delete_listing, name='delete-listing'),
]