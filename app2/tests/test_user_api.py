# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.user import User  # noqa: F401


def test_get_user_by_name(client: TestClient):
    """Test case for get_user_by_name

    Get user by user name
    """
    params = [("with_email", True),     ("pretty_print", True)]
    headers = {
        "api_key": "special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/users/{username}".format(username='username_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_user(client: TestClient):
    """Test case for update_user

    Updated user
    """
    user = {"first_name":"firstName","last_name":"lastName","email":"email","username":"username"}
    params = [("pretty_print", True)]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/users/{username}".format(username='username_example'),
    #    headers=headers,
    #    json=user,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

