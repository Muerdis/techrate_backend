"""
Tag serializer
"""
from rest_framework import serializers

from post.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Tag serializer
    """

    class Meta:
        model = Tag
        fields = "__all__"
