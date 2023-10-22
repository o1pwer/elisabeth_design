from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from database import get_db
from models import User as UserModel
from routers.functions.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, \
    get_current_active_user, get_password_hash
from schemas.user import Token, RegisterUser, User, OAuth2RequestJSON

user_router = APIRouter()


@user_router.post("/users/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2RequestJSON
):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.post("/users/register")
async def register_user(
        user: RegisterUser
):
    if not (fields := user.model_dump(exclude_none=True)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No user data provided for registration process.")
    user_db = get_db(UserModel)
    if await user_db.exists(UserModel.username == user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with that name already exists!.")
    fields['password'] = get_password_hash(fields['password'])
    user_object = await user_db.add(**fields)
    return JSONResponse(
        content={'message': 'User successfully registered', 'user_id': user_object.id},
        status_code=status.HTTP_200_OK,
    )

@user_router.get("/users/me/", response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@user_router.get("/users/me/items/")
async def read_own_items(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]
    # this will contain some logic for item extraction later
