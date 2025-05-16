# tests/test_celery.py
import pytest

from core.celery import app as celery_app


@pytest.mark.django_db
def test_celery_config():
    assert celery_app.conf.timezone == "UTC"


@pytest.mark.django_db
def test_beat_schedule():
    schedule = celery_app.conf.beat_schedule
    assert "check_due_tasks" in schedule
    assert (
        schedule["check_due_tasks"]["task"]
        == "apps.task_manager.api.v1.tasks.check_due_tasks"
    )
    assert schedule["check_due_tasks"]["schedule"].run_every.total_seconds() == 60  # noqa: PLR2004


@pytest.mark.django_db
def test_autodiscover_tasks():
    registered_tasks = celery_app.tasks.keys()
    assert "apps.task_manager.api.v1.tasks.check_due_tasks" in registered_tasks
    assert "apps.task_manager.api.v1.tasks.send_single_message" in registered_tasks
