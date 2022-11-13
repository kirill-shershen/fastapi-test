from injector import singleton

from src.auth.utils import JWTBearer


def configure(binder):
    # repositories
    binder.bind(JWTBearer, to=JWTBearer, scope=singleton)
