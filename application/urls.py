from django.contrib import admin
from django.urls import path,include
from .views import home, url_redirect

urlpatterns = [
    path('',home, name="homepage"),
    path('<str:short_url_code>/',url_redirect, name="surl"),
]