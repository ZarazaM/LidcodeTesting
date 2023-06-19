from pydantic import Field

from settings import base_settings
from utils.models.base_model import BaseModel


class AuthUser(BaseModel):
    login: str = Field(default=base_settings.user.login)
    password: str = Field(default=base_settings.user.password)


class Authentication(BaseModel):
    auth_token: str | None
    user: AuthUser | None = AuthUser()
