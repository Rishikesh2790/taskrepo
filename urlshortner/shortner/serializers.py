from rest_framework import serializers
from . models import ShortUrl
class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ['long_url']