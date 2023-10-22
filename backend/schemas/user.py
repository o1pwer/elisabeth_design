from pydantic import BaseModel


# AUTH
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class OAuth2RequestJSON(BaseModel):
    username: str
    password: str


# USER
class User(BaseModel):
    username: str
    email: str | None = None

    # disabled: bool | None = None

    class Config:
        from_attributes = True


class UserInDB(User):
    password: str


class RegisterUser(UserInDB):
    pass
