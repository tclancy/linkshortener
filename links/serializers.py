from rest_framework import serializers
from links.models import ShortenedLink


class ShortenedLinkSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ShortenedLink
        fields = ("id", "url", "mobile_url", "tablet_url", "shortened", "hits")
        read_only_fields = ("id", "shortened", "hits",)
