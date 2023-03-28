from datetime import datetime, timedelta

import jwt

from utils.settings import settings


def create_access_token(data: str):
    expiry = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {"exp": expiry, "user": str(data)}
    access_token = jwt.encode(payload, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    return access_token


def create_refresh_token(data: str):
    expiry = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    payload = {"exp": expiry, "user": str(data)}
    refresh_token = jwt.encode(payload, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
    return refresh_token
