from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny

from apps.task_manager.models import Task
from core import docstring
from core.views import BaseAPIView

from .serializers import TaskCreateSerializer, TaskSerializer, TaskUpdateSerializer


@docstring.auto_docstring()
@extend_schema(tags=("tasks",))
@extend_schema_view(
    get=extend_schema(summary="Получение списка задач"),
)
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

    filter_backends = (filters.SearchFilter,)

    search_fields = ("telegram_user_id",)


@extend_schema(tags=("tasks",))
@extend_schema_view(
    post=extend_schema(summary="Создание задачи"),
)
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = (AllowAny,)


@extend_schema(tags=("tasks",))
@extend_schema_view(
    get=extend_schema(summary="Получение задачи"),
    patch=extend_schema(summary="Обновление статуса задачи"),
)
class TaskRetrieveUpdateView(BaseAPIView, generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ("get", "patch")
    serializer_classes = {  # noqa: RUF012
        "GET": TaskSerializer,
        "PATCH": TaskUpdateSerializer,
    }
