# listings/models.py

from django.db import models

class Listing(models.Model):
    directory_name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, null=True, blank=True)
    directory_url = models.CharField(max_length=255)
    industry_niche = models.CharField(max_length=100)
    social_media_links = models.JSONField()
    description = models.TextField()
    keywords = models.TextField()
    video_url = models.URLField(null=True, blank=True)
    logo = models.FileField(upload_to='logos/')
    email = models.EmailField()

    def __str__(self):
        return self.directory_name
