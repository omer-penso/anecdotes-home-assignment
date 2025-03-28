import pytest
from auth import login


def test_login_should_succeed():
    result = login("emilys", "emilyspass")
    assert result is not None
    assert "accessToken" in result


def test_login_should_fail():
    result = login("omerp", "omer1234")
    assert result is None
