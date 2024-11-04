from pathlib import Path
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Gateway of the App"}


def test_spec():
    response = client.get("/openapi.yaml")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/yaml; charset=utf-8"

    try:
        expected_yaml = Path("expected-openapi.yaml").read_text()
        assert response.text == expected_yaml
    except FileNotFoundError:
        print("Expected OpenAPI specification file not found.")

        with open("expected-openapi.yaml", "w") as f:
            f.write(response.text)

        assert False


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_echo():
    response = client.post("/echo", json={"body": "Hello, World!"})

    assert response.status_code == 200
    assert response.json() == "Hello, World!"


def test_get_user():
    response = client.get("/users/frank")

    assert response.status_code == 200
    assert response.json()["username"] == "frank"


def test_update_user():
    response = client.put("/users/jane", json={"username": "jane"})

    assert response.status_code == 200
