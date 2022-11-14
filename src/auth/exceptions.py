from dataclasses import dataclass
from dataclasses import field

from fastapi import HTTPException
from starlette import status


@dataclass
class CredentialsException(HTTPException):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    detail: str = "Could not validate credentials"
    headers: dict = field(default_factory=lambda: {"WWW-Authenticate": "Bearer"})


@dataclass
class ForbiddenException(HTTPException):
    status_code: int = status.HTTP_403_FORBIDDEN
    detail: str = "Forbidden"
    headers: dict = field(default_factory=lambda: {"WWW-Authenticate": "Bearer"})
