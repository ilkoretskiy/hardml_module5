import pytest

from fastapi.testclient import TestClient

from impl import main



def test_should_update_storage_on_startup(mocker):
    with mocker.patch("impl.main.retrieve_secret_value", return_value = 15):
        with TestClient(main.app) as client:
            assert main.storage['secret_number'] == 15


def test_shouldnt_update_storage_when_api_doesnt_respond(mocker):
    with mocker.patch("impl.main.retrieve_secret_value", return_value = None ):
        with TestClient(main.app) as client:
            assert main.storage['secret_number'] is None


def test_should_return_secret_number(mocker):    
    with mocker.patch("impl.main.retrieve_secret_value", return_value = 15):
        with TestClient(main.app) as client:
            response = client.get("return_secret_number")

            assert response.status_code == 200
            result = response.json()

            assert "secret_number" in  result
            assert result['secret_number'] == 15
