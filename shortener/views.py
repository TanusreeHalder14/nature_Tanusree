import random
import string
from django.shortcuts import get_object_or_404, redirect, render

from .models import ShortenedURL

# Create your views here.
def home(request):
    short_url = None
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        # Logic to create and save shortened URL would go here
        code=''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ShortenedURL.objects.create(original_url=original_url, short_url=code)
        short_url = request.build_absolute_uri('/') + code
    return render(request, 'home.html', {'short_url': short_url})
def redirect_short_url(request, code):
    # Logic to retrieve the original URL from the short code would go here
    url = get_object_or_404(ShortenedURL, short_url=code)
    return redirect(url.original_url)