from typing import TypedDict

from pydantic import BaseModel, Field

from utils.fakers import random_string, random_number, random_id, random_link


class UpdateOrganizer(BaseModel):
    link: str | None = Field(default_factory=random_string)
    name: str | None = Field(default_factory=random_string)
    forSorted: None | int = Field(default_factory=random_number)


class DefaultOrganizer(BaseModel):
    id: str = Field(default_factory=random_id)
    link: str = Field(default_factory=random_link)
    name: str = Field(default_factory=random_string)
    forSorted: None | int = Field(default_factory=random_number)


class DefaultOrganizersList(BaseModel):
    Items: list[DefaultOrganizer]
    CountList: int


class OrganizerDict(TypedDict):
    id: str
    link: str
    name: str
    forSorted: int
