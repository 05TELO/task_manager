from django.urls import include, path

urls_v1 = [
    path("", include("apps.task_manager.api.v1.urls")),
]
