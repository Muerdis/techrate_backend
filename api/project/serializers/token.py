"""
Token serializer
"""
from rest_framework import serializers

from api.project.serializers import BlockchainSerializer
from project.models import Token


class TokenSerializer(serializers.ModelSerializer):
    """
    Token serializer
    """
    blockchain = BlockchainSerializer(many=False)
    image = serializers.SerializerMethodField(help_text="Image")

    class Meta:
        model = Token
        fields = "__all__"

    @staticmethod
    def get_image(obj):
        return f"https://techrate.org{obj.image.url}" if obj.image else None
