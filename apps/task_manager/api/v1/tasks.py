import logging
import time

import httpx
from celery import shared_task
from django.utils import timezone

from apps.task_manager.models import Task
from core.config import settings

logger = logging.getLogger(__name__)


@shared_task(
    autoretry_for=(Exception,),
    retry_backoff=10,
    retry_kwargs={"max_retries": 5},
    soft_time_limit=10000,
)
def send_single_message(chat_id: int, message: str) -> str:
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}

    try:
        time.sleep(1)

        with httpx.Client(timeout=httpx.Timeout(20.0)) as client:
            response = client.post(url, json=payload)
            response.raise_for_status()

    except httpx.HTTPStatusError as e:
        if e.response.status_code == httpx.codes.TOO_MANY_REQUESTS:
            sleep_time = e.response.json().get("parameters", {}).get("retry_after", 5)
            logger.warning(
                f"Rate limit hit for {chat_id}. Sleeping for {sleep_time} seconds..."
            )
            time.sleep(sleep_time)
            msg = f"Rate limited. Retry after {sleep_time} sec"
            raise TimeoutError(msg) from e

        return f"HTTP ERROR - {chat_id=}: {e!s}"

    except httpx.RequestError as e:
        return f"REQUEST ERROR - {chat_id=}: {e!s}"
    else:
        return f"OK - {chat_id=}"


@shared_task
def check_due_tasks() -> str:
    now = timezone.now()
    soon = now + timezone.timedelta(minutes=10)

    due_tasks = Task.objects.filter(
        deadline__gte=now, deadline__lte=soon, status=Task.Status.UNDONE
    )

    for task in due_tasks:
        send_single_message.delay(
            chat_id=task.telegram_user_id,
            message=f'⏰ Срок выполнения задачи "{task.title}"'
            f" истекает в {task.deadline.strftime('%H:%M')}!",
        )
    return "Done"
