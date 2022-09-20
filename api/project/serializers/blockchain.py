"""
Blockchain serializer
"""
from rest_framework import serializers

from project.models import Blockchain


class BlockchainSerializer(serializers.ModelSerializer):
    """
    Blockchain serializer
    """
    image = serializers.SerializerMethodField(help_text="Image")

    class Meta:
        model = Blockchain
        fields = "__all__"

    @staticmethod
    def get_image(obj):
        return f"https://techrate.org{obj.image.url}" if obj.image else None
