from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from apps.task_manager.models import Task


def create_tasks(telegram_user_id: str, fake: Faker) -> None:
    Task.objects.all().delete()
    for _ in range(5):
        minutes = fake.random_int(min=5, max=15)
        Task.objects.create(
            title=fake.sentence(),
            description=fake.paragraph(),
            deadline=timezone.now() + timezone.timedelta(minutes=minutes),
            telegram_user_id=telegram_user_id,
        )


class Command(BaseCommand):
    help = "Sets telegram_user_id for a specific task"

    def add_arguments(self, parser):
        parser.add_argument("telegram_id", type=int, help="Telegram user ID to set")

    def handle(self, *args, **kwargs):
        telegram_id = kwargs["telegram_id"]
        fake = Faker("ru_RU")
        create_tasks(telegram_id, fake)
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully create tasks for telegram_user_id={telegram_id}"
            )
        )
