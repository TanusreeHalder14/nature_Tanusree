from django.urls import path

from .views import home, redirect_short_url

urlpatterns = [
    path('',home, name='home'),
    path('<str:code>', redirect_short_url, name='redirect_short_url'),
]