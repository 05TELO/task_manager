import pytest

from rest_framework.test import APIClient

from apps.task_manager.api.v1.tests.factories import TaskFactory


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def task() -> TaskFactory:
    return TaskFactory.create()
    

