"""
Project API's urls
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.project.views import TokenViewSet, RequestAuditView, LastTokenViewSet, TopLastTokenViewSet

app_name = "project_api"

router = DefaultRouter()
router.register("all", TokenViewSet, basename="tokens")
router.register("last", LastTokenViewSet, basename="last")
router.register("top-last", TopLastTokenViewSet, basename="top_last")

urlpatterns = [
    path("request-audit", RequestAuditView.as_view(), name="request_audit"),
    path("", include(router.urls)),
]
