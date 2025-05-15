import pytest
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from faker import Faker
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

fake = Faker("ru_RU")

URL = reverse("v1:task-list-create")

data = {
    "title": fake.sentence(),
    "description": fake.sentence(),
    "deadline": fake.date_time(tzinfo=timezone.get_current_timezone()),
    "telegram_user_id": fake.random_int(max=9999999999),
}
format = "json"


@pytest.mark.django_db
def test_task_create(
    api_client: APIClient,
) -> None:
    response: Response = api_client.post(URL, data, format)

    assert response.data.get("errors") is None
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == data["title"]
    assert response.data["description"] == data["description"]
    deadline_from_api = parse_datetime(response.data["deadline"])
    assert deadline_from_api == data["deadline"]
    assert response.data["telegram_user_id"] == data["telegram_user_id"]
