# listings/serializers.py

from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    directory_name = serializers.CharField(max_length=255)
    tagline = serializers.CharField(max_length=255, required=False)
    directory_url = serializers.URLField()
    industry_niche = serializers.CharField(max_length=255)
    social_media_links = serializers.JSONField()
    description = serializers.CharField()
    keywords = serializers.CharField()
    video_url = serializers.URLField(required=False)
    logo = serializers.ImageField(required=False)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Listing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.directory_name = validated_data.get('directory_name', instance.directory_name)
        instance.tagline = validated_data.get('tagline', instance.tagline)
        instance.directory_url = validated_data.get('directory_url', instance.directory_url)
        instance.industry_niche = validated_data.get('industry_niche', instance.industry_niche)
        instance.social_media_links = validated_data.get('social_media_links', instance.social_media_links)
        instance.description = validated_data.get('description', instance.description)
        instance.keywords = validated_data.get('keywords', instance.keywords)
        instance.video_url = validated_data.get('video_url', instance.video_url)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
