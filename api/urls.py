"""
API's urls
"""
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = "api"

SchemaView = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Internal API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("swagger/", SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", SchemaView.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    path("post/", include("api.post.urls", namespace="post_api")),
    path("token/", include("api.project.urls", namespace="project_api")),
]
