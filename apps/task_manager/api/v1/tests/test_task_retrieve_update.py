import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from apps.task_manager.api.v1.tests.factories import TaskFactory

fake = Faker("ru_RU")

format = "json"
URL = "v1:task-retrieve-update"


@pytest.mark.django_db
def test_get_task(
    api_client: APIClient,
    task: TaskFactory,
) -> None:
    url = reverse(URL, kwargs={"pk": task.id})
    response: Response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("id") == task.id
    assert response.data.get("title") == task.title
    assert response.data.get("description") == task.description
    assert response.data.get("status") == task.status


@pytest.mark.django_db
def test_update_task(
    api_client: APIClient,
    task: TaskFactory,
) -> None:
    url = reverse(URL, kwargs={"pk": task.id})
    data = {"status": "done"}
    response: Response = api_client.patch(url, data, format)

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("status") == data["status"]
