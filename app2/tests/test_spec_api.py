# coding: utf-8

from fastapi.testclient import TestClient




def test_get_open_api_spec_yaml(client: TestClient):
    """Test case for get_open_api_spec_yaml

    Get the OpenAPI spec in YAML format
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/openapi.yaml",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

