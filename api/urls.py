
from django.urls import path,include
from .views import make_url_short

urlpatterns = [
    path('create/',make_url_short),
]