# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.spec_api_base import BaseSpecApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/openapi.yaml",
    responses={
        200: {"model": str, "description": "The OpenAPI YAML specification"},
    },
    tags=["Spec"],
    summary="Get the OpenAPI spec in YAML format",
    response_model_by_alias=True,
)
async def get_open_api_spec_yaml(
) -> str:
    if not BaseSpecApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSpecApi.subclasses[0]().get_open_api_spec_yaml()
