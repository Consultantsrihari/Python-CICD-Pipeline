# tests/test_app.py
import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_route(client):
    """Test the main hello route."""
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["message"] == "Hello, World! This is a Python CI/CD demo."

def test_health_check_route(client):
    """Test the health check route."""
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "ok"