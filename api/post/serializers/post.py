"""
Post serializer
"""
from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer
    """
    tags = serializers.SerializerMethodField(help_text="tags")
    image = serializers.SerializerMethodField(help_text="Image")

    class Meta:
        model = Post
        fields = "__all__"

    @staticmethod
    def get_tags(obj):
        tags = obj.tags.values_list("name", flat=True)
        return tags or []

    @staticmethod
    def get_image(obj):
        return obj.replace("http://83.220.175.158:8000/", "https://techrate.org/")
