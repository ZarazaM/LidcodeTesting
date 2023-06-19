from typing import TypedDict

from pydantic import BaseModel, Field

from utils.fakers import random_string, random_number, random_id, random_link


class UpdateMaterial(BaseModel):
    # file:
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    link: str = Field(default_factory=random_link)
    name: str = Field(default_factory=random_string)


class DefaultMaterial(BaseModel):
    id: str = Field(default_factory=random_id)
    # file:
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    link: str = Field(default_factory=random_link)
    name: str = Field(default_factory=random_string)


class DefaultMaterialsList(BaseModel):
    Items: list[DefaultMaterial]
    CountList: int


class MaterialDict(TypedDict):
    id: str
    forSorted: int
    link: str
    name: str
