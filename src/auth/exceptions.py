from dataclasses import dataclass

from fastapi import HTTPException
from starlette import status


@dataclass
class CredentialsException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Could not validate credentials"
    headers = {"WWW-Authenticate": "Bearer"}


@dataclass
class ForbiddenException(HTTPException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Forbidden"
    headers = {"WWW-Authenticate": "Bearer"}
