from rest_framework import serializers
from links.models import ShortenedLink


class ShortenedLinkSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ShortenedLink
        fields = ("url", "mobile_url", "tablet_url", "hits")
        read_only_fields = ("hits",)
