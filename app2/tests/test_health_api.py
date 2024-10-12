# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.health_check200_response import HealthCheck200Response  # noqa: F401


def test_health_check(client: TestClient):
    """Test case for health_check

    Health check of the service
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/health",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

