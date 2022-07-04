"""
Token serializer
"""
from rest_framework import serializers

from project.models import Token


class TokenSerializer(serializers.ModelSerializer):
    """
    Token serializer
    """

    class Meta:
        model = Token
        fields = "__all__"
