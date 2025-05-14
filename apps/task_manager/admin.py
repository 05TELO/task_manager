from django.contrib import admin

from apps.task_manager.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "deadline",
        "telegram_user_id",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status",)
    search_fields = ("title", "description", "telegram_user_id")
    readonly_fields = ("created_at", "updated_at")
