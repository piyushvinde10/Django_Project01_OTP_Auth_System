"""
URL configuration for otp_project project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls")),
]