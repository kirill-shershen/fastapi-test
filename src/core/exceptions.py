from dataclasses import dataclass

from fastapi import HTTPException
from fastapi import status


@dataclass
class BadRequest(HTTPException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "Incorrectly filled in data"
