# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2024-10-07T11:50:15+00:00

from __future__ import annotations

from fastapi import APIRouter

from ..dependencies import *

router = APIRouter(tags=['Spec'])


@router.get('/openapi.yaml', response_model=str, tags=['Spec'])
def get_open_a_p_i_spec_yaml() -> str:
    """
    Get the OpenAPI spec in YAML format
    """
    pass
