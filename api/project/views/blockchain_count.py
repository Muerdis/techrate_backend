"""
Blockchains count view set
"""
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import Blockchain


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_id="Blockchains count",
        operation_description="Blockchains count",
    ),
)
class BlockchainsCountView(APIView):
    """
    API for blockchains count
    """

    permission_classes = (AllowAny,)

    def get(self, request, **kwargs):
        """
        Blockchains count
        """
        return Response({"blockchains_count": Blockchain.objects.count()}, status=status.HTTP_200_OK)
