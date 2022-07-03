"""
Request audit serializer
"""
from rest_framework import serializers


class RequestAuditSerializer(serializers.Serializer):
    """
    Request audit serializer
    """

    name = serializers.CharField(help_text="name", max_length=200, required=False)
    email = serializers.EmailField(help_text="email", max_length=200, required=False)
    contact = serializers.CharField(help_text="email", max_length=500, required=True)
    comments = serializers.CharField(help_text="email", max_length=1000, required=False)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
