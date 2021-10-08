from rest_framework import serializers
from application.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['long_url']
        