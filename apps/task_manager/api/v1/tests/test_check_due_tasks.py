import pytest
from django.utils import timezone
from pytest_mock import MockerFixture

from apps.task_manager.api.v1.tasks import check_due_tasks
from apps.task_manager.models import Task


@pytest.mark.django_db
def test_check_due_tasks(mocker: MockerFixture):
    now = timezone.now()
    soon = now + timezone.timedelta(minutes=10)

    task = Task.objects.create(
        title="Urgent task",
        description="Test description",
        deadline=soon,
        telegram_user_id=123456789,
        status=Task.Status.UNDONE,
    )

    mock_delay = mocker.patch(
        "apps.task_manager.api.v1.tasks.send_single_message.delay"
    )

    result = check_due_tasks()

    assert result == "Done"
    mock_delay.assert_called_once_with(
        chat_id=task.telegram_user_id,
        message=f'⏰ Срок выполнения задачи "{task.title}"'
        f" истекает в {timezone.localtime(soon).strftime('%H:%M')}!",
    )
