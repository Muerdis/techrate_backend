"""
Post serializer
"""
from rest_framework import serializers

from api.post.serializers import TagSerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer
    """
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
