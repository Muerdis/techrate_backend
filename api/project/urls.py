"""
Project API's urls
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.project.views import TokenViewSet

app_name = "project_api"

router = DefaultRouter()
router.register("all", TokenViewSet, basename="tokens")

urlpatterns = [
    path("", include(router.urls)),
]
