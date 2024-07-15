from django.contrib import admin
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Root URL should be an empty string
    path('about-me/', AboutPageView.as_view(), name='about')
]
