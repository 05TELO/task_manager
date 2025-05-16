import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

URL = reverse("healthcheck")


@pytest.mark.django_db
def test_healthcheck(
    api_client: APIClient,
) -> None:
    response: Response = api_client.get(URL)

    assert response.status_code == status.HTTP_200_OK
