from typing import TypedDict

from pydantic import BaseModel, Field

from utils.fakers import random_string, random_number, random_id, random_link, random_event_status


class UpdateTeam(BaseModel):
    # event_id: str
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    name: str = Field(default_factory=random_string)
    status: str = Field(default_factory=random_event_status)


class DefaultTeam(BaseModel):
    id: str = Field(default_factory=random_id)
    # event_id: str
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    name: str = Field(default_factory=random_string)
    status: str = Field(default_factory=random_event_status)


class DefaultTeamsList(BaseModel):
    Items: list[DefaultTeam]
    CountList: int


class TeamDict(TypedDict):
    id: str
    forSorted: int
    name: str
    status: str
