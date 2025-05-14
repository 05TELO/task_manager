from django.urls import path

from .views import TaskCreateView, TaskListView, TaskRetrieveUpdateView

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/", TaskRetrieveUpdateView.as_view(), name="task-retrieve-update"
    ),
]
