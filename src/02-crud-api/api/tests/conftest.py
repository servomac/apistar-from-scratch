import pytest

from apistar.test import TestClient


@pytest.fixture(scope="session")
def client():
    return TestClient()
