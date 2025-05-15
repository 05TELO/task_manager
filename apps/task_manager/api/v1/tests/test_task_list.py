import pytest
from django.urls import reverse
from django.utils.dateparse import parse_datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from apps.task_manager.api.v1.tests.factories import TaskFactory

URL = reverse("v1:task-list-create")


@pytest.mark.django_db
def test_task_list(
    api_client: APIClient,
    task: TaskFactory,
) -> None:
    response: Response = api_client.get(URL)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
    result = response.data["results"][0]
    assert result["title"] == task.title
    assert result["description"] == task.description
    deadline_from_api = parse_datetime(result["deadline"])
    assert deadline_from_api == task.deadline
    assert result["telegram_user_id"] == task.telegram_user_id
    assert result["status"] == task.status

    response = api_client.get(URL, {"search": task.telegram_user_id})

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
    result = response.data["results"][0]
    assert result["title"] == task.title
    assert result["description"] == task.description
    deadline_from_api = parse_datetime(result["deadline"])
    assert deadline_from_api == task.deadline
    assert result["telegram_user_id"] == task.telegram_user_id
    assert result["status"] == task.status
