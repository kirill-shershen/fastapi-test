from fastapi import HTTPException
from fastapi import status


class BadRequest(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Incorrectly filled in data"
