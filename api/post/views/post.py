"""
Post view set
"""
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.post.serializers import PostSerializer
from post.models import Post


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Get a list posts",
        operation_description="Get a list of posts",
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="Get a post",
        operation_description="Get a post",
    ),
)
class PostViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    PageNumberPagination,
    viewsets.GenericViewSet
):
    """
    API for getting roles
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    page_size_query_param = "size"
    page_size = 3
    max_page_size = 10000

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        tag = request.query_params.get("tag", None)
        if tag:
            queryset = queryset.filter(tags__name=tag)

        page = self.paginate_queryset(queryset, self.request)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
