"""
Request audit view
"""
import asyncio

import telegram
from django.conf import settings
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.project.serializers import RequestAuditSerializer


async def send_message(data):
    bot = telegram.Bot(settings.BOT_TOKEN)
    async with bot:
        await bot.send_message(text=data, chat_id=settings.CHAT_ID)


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_id="Request audit",
        operation_description="Request audit",
    ),
)
class RequestAuditView(APIView):
    """
    API for request audit
    """

    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        """
        Request audit
        """

        serializer = RequestAuditSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        asyncio.run(send_message(request.data))

        return Response({"status": "success"}, status=status.HTTP_200_OK)
