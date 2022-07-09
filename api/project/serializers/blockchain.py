"""
Blockchain serializer
"""
from rest_framework import serializers

from project.models import Blockchain


class BlockchainSerializer(serializers.ModelSerializer):
    """
    Blockchain serializer
    """

    class Meta:
        model = Blockchain
        fields = "__all__"
