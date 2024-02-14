import requests_mock
import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("BASE_URL")


def fetch_data():
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@pytest.fixture
def mock():
    with requests_mock.Mocker() as m:
        yield m


def test_fetch_data_success(mock):
    mock_response = {"key": "value"}
    mock.get(base_url, json=mock_response)

    result = fetch_data()

    assert result == mock_response


@pytest.mark.parametrize("status_code", [400, 404, 500])
def test_fetch_data_error(status_code, mock):
    mock.get(base_url, status_code=status_code)

    result = fetch_data()

    assert result is None