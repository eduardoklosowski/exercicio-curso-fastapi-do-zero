from datetime import datetime, timedelta
from http import HTTPStatus
from zoneinfo import ZoneInfo

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User

SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode['exp'] = datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_current_user(session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if not username:
            raise credentials_exception
    except jwt.DecodeError:
        raise credentials_exception

    user = session.scalar(select(User).where(User.email == username))

    if not user:
        raise credentials_exception

    return user
