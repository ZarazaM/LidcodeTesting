from typing import TypedDict

from pydantic import BaseModel, Field

from utils.fakers import random_string, random_number, random_id, random_link


class UpdateSponsor(BaseModel):
    link: str | None = Field(default_factory=random_string)
    name: str | None = Field(default_factory=random_string)
    forSorted: None | int = Field(default_factory=random_number)
    # imageDef: None | str = Field(default_factory=random_link)
    # imageHor: None | str = Field(default_factory=random_link)
    # imageVer: None | str = Field(default_factory=random_link)


class DefaultSponsor(BaseModel):
    id: str = Field(default_factory=random_id)
    link: str = Field(default_factory=random_link)
    name: str = Field(default_factory=random_string)
    forSorted: int = Field(default_factory=random_number)
    # imageDef: None | str = Field(default_factory=random_link)
    # imageHor: None | str = Field(default_factory=random_link)
    # imageVer: None | str = Field(default_factory=random_link)


class DefaultSponsorsList(BaseModel):
    # __root__: list[DefaultSponsor]
    Items: list[DefaultSponsor]
    CountList: int


class SponsorDict(TypedDict):
    id: str
    link: str
    name: str
    forSorted: int
    # imageDef: str
    # imageHor: str
    # imageVer: str
