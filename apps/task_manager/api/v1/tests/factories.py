import factory
from django.utils import timezone
from factory.django import DjangoModelFactory

from apps.task_manager.models import Task


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker("sentence", nb_words=5, locale="ru_RU")
    description = factory.Faker("paragraph", nb_sentences=5, locale="ru_RU")
    deadline = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    telegram_user_id = factory.Faker("pyint", max_value=9999999999)
    status = factory.Iterator(Task.Status.values)
