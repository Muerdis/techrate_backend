"""
Token view set
"""
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.project.serializers import TokenSerializer
from project.models import Token


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Get a list of tokens",
        operation_description="Get a list of tokens",
    ),
)
class TokenViewSet(
    mixins.ListModelMixin,
    PageNumberPagination,
    viewsets.GenericViewSet
):
    """
    API for getting tokens
    """

    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)
    page_size_query_param = "size"
    page_size = 20
    max_page_size = 10000
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["contract_address"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        search = request.query_params.get("search", "")
        field = request.query_params.get("field", "")
        sort = request.query_params.get("sort", "")
        if search:
            queryset = queryset.filter(name__icontains=search)

        blockchain = request.query_params.get("blockchain", None)
        if blockchain:
            queryset = queryset.filter(blockchain__name=blockchain)

        if field and sort:
            if field == "blockchain":
                field = "blockchain__name"

            if sort == "asc":
                queryset = queryset.order_by("-is_partner", field)
            elif sort == "desc":
                queryset = queryset.order_by("-is_partner", f"-{field}")
        else:
            queryset = queryset.order_by("-is_partner", "-created")

        page = self.paginate_queryset(queryset, self.request)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
