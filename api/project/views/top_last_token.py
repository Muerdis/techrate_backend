"""
Top last token view set
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
        operation_id="Get a list of top last tokens",
        operation_description="Get a list of top last tokens",
    ),
)
class TopLastTokenViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    API for getting top last tokens
    """

    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        uids = Token.objects.values_list("uid", flat=True)[:10]
        return Token.objects.filter(uid__in=uids).order_by("-score")[:3]
