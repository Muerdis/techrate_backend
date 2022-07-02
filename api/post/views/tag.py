"""
Tag view set
"""
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.post.serializers import TagSerializer
from post.models import Tag


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Get a list of tags",
        operation_description="Get a list of tags",
    ),
)
class TagViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    API for getting posts
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
