import pytest
from auth import login, get_authenticated_user


def test_login_should_succeed():
    result = login("emilys", "emilyspass")
    assert result is not None
    assert "accessToken" in result


def test_login_should_fail():
    result = login("omerp", "omer1234")
    assert result is None


def test_get_authenticated_user_should_success():
    credentials = {"username": "emilys", "password": "emilyspass"}
    tokens = login(**credentials)
    assert tokens is not None, "Login failed, no tokens returned"

    user = get_authenticated_user(tokens["accessToken"])
    assert user is not None, "Failed to fetch authenticated user"
    assert user["username"] == credentials["username"]


def test_get_authenticated_user_invalid_token():
    user = get_authenticated_user("invalid_token")
    assert user is None