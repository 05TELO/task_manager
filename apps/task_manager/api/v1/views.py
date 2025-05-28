from typing import ClassVar
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny

from apps.task_manager.models import Task
from core.views import BaseAPIView

from .serializers import TaskCreateSerializer, TaskSerializer, TaskUpdateSerializer


@extend_schema(tags=("tasks",))
@extend_schema_view(
    get=extend_schema(
        summary="Получение списка задач",
        description="```search``` поиск по полям:\n\n * telegram_user_id",
        parameters=[
            OpenApiParameter(
                name="search", type=str, description="Поиск по telegram_user_id"
            ),
        ],
    ),
    post=extend_schema(summary="Создание задачи"),
)
class TaskListCreateView(BaseAPIView, generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)
    serializer_classes: ClassVar[dict[str, type[object]]] = {
        "GET": TaskSerializer,
        "PATCH": TaskCreateSerializer,
    }

    filter_backends = (filters.SearchFilter,)

    search_fields = ("telegram_user_id",)


@extend_schema(tags=("tasks",))
@extend_schema_view(
    get=extend_schema(summary="Получение задачи"),
    patch=extend_schema(summary="Обновление статуса задачи"),
)
class TaskRetrieveUpdateView(BaseAPIView, generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ("get", "patch")
    serializer_classes: ClassVar[dict[str, type[object]]] = {
        "GET": TaskSerializer,
        "PATCH": TaskUpdateSerializer,
    }
