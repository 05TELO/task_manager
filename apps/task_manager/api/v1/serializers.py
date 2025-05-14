# tasks/serializers.py
from rest_framework import serializers

from apps.task_manager.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "deadline",
            "telegram_user_id",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "deadline",
            "telegram_user_id",
        )


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("status",)
