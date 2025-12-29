from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=8, unique=True)
    # expired_at = models.DateTimeField(auto_now_add=True)
