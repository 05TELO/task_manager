import datetime
import os

from celery import Celery
from celery.schedules import schedule

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# Load task modules from all registered Django apps.
app.autodiscover_tasks(packages=["apps.task_manager.api.v1"])

# Set timezone to local
app.conf.timezone = "UTC"

app.conf.beat_schedule = {
    "check_due_tasks": {
        "task": "apps.task_manager.api.v1.tasks.check_due_tasks",
        "schedule": schedule(run_every=datetime.timedelta(seconds=60)),
    },
}
