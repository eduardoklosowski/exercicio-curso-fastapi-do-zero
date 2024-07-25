import pytest
from fast_zero.app import app
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    return TestClient(app)
