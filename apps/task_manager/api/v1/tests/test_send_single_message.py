import httpx
import pytest
from pytest_mock import MockerFixture

from apps.task_manager.api.v1.tasks import send_single_message


@pytest.mark.django_db
def test_send_single_message_success(mocker: MockerFixture):
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status.return_value = None

    mock_post = mocker.patch("httpx.Client.post", return_value=mock_response)

    result = send_single_message(chat_id=123, message="Test message")
    assert result == "OK - chat_id=123"
    mock_post.assert_called_once()


@pytest.mark.django_db
def test_send_single_message_rate_limit(mocker: MockerFixture):
    mocker.patch(
        "httpx.Client.post",
        side_effect=httpx.HTTPStatusError(
            "Rate limited",
            request=mocker.MagicMock(),
            response=mocker.MagicMock(
                status_code=429, json=lambda: {"parameters": {"retry_after": 5}}
            ),
        ),
    )
    mocker.patch("time.sleep")

    with pytest.raises(TimeoutError):
        send_single_message(chat_id=123, message="Test message")


@pytest.mark.django_db
def test_other_http_errors(mocker: MockerFixture):
    mock_error = httpx.HTTPStatusError(
        "Not Found",
        request=mocker.MagicMock(),
        response=mocker.MagicMock(status_code=404),
    )

    mocker.patch("httpx.Client.post", side_effect=mock_error)

    result = send_single_message(chat_id=123, message="Test")

    assert result == "HTTP ERROR - chat_id=123: Not Found"


@pytest.mark.django_db
def test_request_errors(mocker: MockerFixture):
    mock_error = httpx.RequestError("Connection failed")

    mocker.patch("httpx.Client.post", side_effect=mock_error)

    result = send_single_message(chat_id=456, message="Test")

    assert result == "REQUEST ERROR - chat_id=456: Connection failed"
