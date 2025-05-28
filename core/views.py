from typing import ClassVar

from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request: Request) -> Response:
        return Response(status=200)


class BaseAPIView:
    serializer_classes: ClassVar[dict[str, type[object]]] = {}

    def get_serializer(self, *args, **kwargs):
        """Choose serializer depending on request method."""
        method = self.request.method
        default = self.serializer_classes.get("GET")
        serializer_class = self.serializer_classes.get(method, default)
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
