"""
Token serializer
"""
from rest_framework import serializers

from project.models import Token


class TokenSerializer(serializers.ModelSerializer):
    """
    Token serializer
    """
    blockchain = serializers.CharField(help_text="Blockchain", source="blockchain.name")

    class Meta:
        model = Token
        fields = "__all__"
