from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from core.views import HealthCheckView

from .v1 import urls_v1

urlpatterns = [
    # Django
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Api
    path(
        "api/",
        include(
            [
                path("v1/", include((urls_v1, "v1"), namespace="v1")),
                path("health", HealthCheckView.as_view(), name="healthcheck"),
            ]
        ),
    ),
]
