from typing import TypedDict

from pydantic import BaseModel, Field

from utils.fakers import random_string, random_number, random_id, random_link, random_user_access


class UpdateUser(BaseModel):
    access: str = Field(default_factory=random_user_access)
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    login: str = Field(default_factory=random_string)
    password: str = Field(default_factory=random_string)


class DefaultUser(BaseModel):
    id: str = Field(default_factory=random_id)
    access: str = Field(default_factory=random_user_access)
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    login: str = Field(default_factory=random_string)
    password: str = Field(default_factory=random_string)


class DefaultUsersList(BaseModel):
    Items: list[DefaultUser]
    CountList: int


class UserDict(TypedDict):
    id: str
    access: str
    forSorted: int
    login: str
    password: str
