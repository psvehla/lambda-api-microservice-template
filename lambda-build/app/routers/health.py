# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2024-10-07T11:50:15+00:00

from __future__ import annotations

from fastapi import APIRouter, status, Response

from ..dependencies import Union, HealthGetResponse, HealthGetResponse1
from app.service import service

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthGetResponse,
    responses={"503": {"model": HealthGetResponse1}},
    tags=["Health"],
)
def health_check(response: Response) -> Union[HealthGetResponse, HealthGetResponse1]:
    """
    Health check of the service
    """
    if service.health_check():
        return HealthGetResponse(status="healthy")
    else:
        response.status_code = (
            status.HTTP_503_SERVICE_UNAVAILABLE
        )  # Set response status code to 503
        return HealthGetResponse1(status="unhealthy")
