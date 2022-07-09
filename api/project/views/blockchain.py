"""
Blockchain view set
"""
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.project.serializers import BlockchainSerializer
from project.models import Blockchain


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Get a list of blockchains",
        operation_description="Get a list of blockchains",
    ),
)
class BlockchainViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    API for getting posts
    """

    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer
    permission_classes = (AllowAny,)
