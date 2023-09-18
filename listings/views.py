from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from auth_app.serializers import CustomUserSerializer


@api_view(['POST'])
def add_listing(request):
    if request.method == 'POST':
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_listings(request):
    if request.method == 'GET':
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def update_listing(request, listing_id):
    try:
        listing = Listing.objects.get(id=listing_id)
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Listing.DoesNotExist:
        return Response({"error": "Listing not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_listing(request, listing_id):
    try:
        listing = Listing.objects.get(id=listing_id)
        listing.delete()
        return Response({"message": "Listing Deleted"})
    except Listing.DoesNotExist:
        return Response({"error": "Listing not found"}, status=status.HTTP_404_NOT_FOUND)
