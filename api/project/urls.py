"""
Project API's urls
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.project.views import TokenViewSet, RequestAuditView

app_name = "project_api"

router = DefaultRouter()
router.register("all", TokenViewSet, basename="tokens")

urlpatterns = [
    path("request-audit", RequestAuditView.as_view(), name="request_audit"),
    path("", include(router.urls)),
]
