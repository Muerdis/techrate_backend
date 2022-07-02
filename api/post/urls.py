"""
Post API's urls
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.post.views import PostViewSet, TagViewSet

app_name = "post_api"

router = DefaultRouter()
router.register("all", PostViewSet, basename="posts")
router.register("tags", TagViewSet, basename="tags")

urlpatterns = [
    path("", include(router.urls)),
]
