from rest_framework import serializers
from apps.shorter.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["url", "token", "link_count"]
