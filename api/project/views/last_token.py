"""
Last token view set
"""
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.project.serializers import TokenSerializer
from project.models import Token


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Get a list of last tokens",
        operation_description="Get a list of last tokens",
    ),
)
class LastTokenViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    API for getting last tokens
    """

    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Token.objects.all()[:3]
