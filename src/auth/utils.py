from datetime import datetime
from datetime import timedelta

from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from jose import ExpiredSignatureError
from jose import jwt
from passlib.context import CryptContext
from passlib.exc import InvalidTokenError

from src.auth.exceptions import CredentialsException
from src.config.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)


def encode_access_token(username: str) -> str:
    payload = {
        "exp": datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes),
        "iat": datetime.utcnow(),
        "scope": "access_token",
        "sub": username,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        if payload["scope"] == "access_token":
            return payload
        raise CredentialsException(detail="Invalid scope for token")
    except jwt.JWSError:
        raise CredentialsException()
    except ExpiredSignatureError:
        raise CredentialsException(detail="Token expired")
    except InvalidTokenError:
        raise CredentialsException(detail="Invalid token")


def encode_refresh_token(username: str) -> str:
    payload = {
        "exp": datetime.utcnow() + timedelta(hours=settings.refresh_token_expire_hours),
        "iat": datetime.utcnow(),
        "scope": "refresh_token",
        "sub": username,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.secret_key, algorithms=[settings.algorithm])
        if payload["scope"] == "refresh_token":
            username = payload["sub"]
            new_token = encode_access_token(username)
            return new_token
        raise CredentialsException(detail="Invalid scope for token")
    except jwt.JWSError:
        raise CredentialsException()
    except ExpiredSignatureError:
        raise CredentialsException(detail="Token expired")
    except InvalidTokenError:
        raise CredentialsException(detail="Invalid token")
