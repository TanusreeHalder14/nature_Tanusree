from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=800, unique=True)
    short_url = models.CharField(max_length=8, unique=True)
    # expired_at = models.DateTimeField(auto_now_add=True)
