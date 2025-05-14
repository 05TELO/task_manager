from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class Status(models.TextChoices):
        UNDONE = "undone"
        DONE = "done"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    telegram_user_id = models.BigIntegerField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.UNDONE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
        ordering = ("deadline",)

    def __str__(self):
        return f"{self.title} (до {self.deadline})"
