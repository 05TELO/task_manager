import pytest
from django.utils import timezone

from apps.task_manager.api.v1.tests.factories import TaskFactory


@pytest.mark.django_db
def test_task_str_representation():
    deadline = timezone.now() + timezone.timedelta(days=1)

    task = TaskFactory(
        title="Важная задача",
        deadline=deadline,
    )

    expected_str = f"Важная задача (до {deadline})"
    assert str(task) == expected_str
