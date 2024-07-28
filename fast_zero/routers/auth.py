from http import HTTPStatus
from typing import Annotated

import sqlalchemy as sa
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import Token
from fast_zero.security import create_access_token, get_current_user, verify_password

router = APIRouter(prefix='/auth', tags=['auth'])

T_OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
T_Session = Annotated[Session, Depends(get_session)]
T_User = Annotated[User, Depends(get_current_user)]


@router.post('/token', status_code=HTTPStatus.OK, response_model=Token)
def login_for_access_token(form_data: T_OAuth2Form, session: T_Session):
    user = session.scalar(sa.select(User).where(User.email == form_data.username))

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Incorrect email or password')

    access_token = create_access_token({'sub': user.email})

    return {'token_type': 'bearer', 'access_token': access_token}


@router.post('/refresh_token', status_code=HTTPStatus.OK, response_model=Token)
def refresh_access_token(user: T_User):
    new_access_token = create_access_token({'sub': user.email})

    return {'token_type': 'bearer', 'access_token': new_access_token}
