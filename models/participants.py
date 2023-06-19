from typing import TypedDict

from pydantic import BaseModel, Field

from utils.fakers import random_string, random_number, random_id, random_bool, random_email, random_phone, random_course


class UpdateParticipant(BaseModel):
    coach: bool = Field(default_factory=random_bool)
    contact: bool = Field(default_factory=random_bool)
    email_address: str = Field(alias='emailAdress', default_factory=random_email)
    # event_id
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    main: bool = Field(default_factory=random_bool)
    name: str = Field(default_factory=random_string)
    organization: str = Field(default_factory=random_string)
    phone_numbers: str = Field(alias='phoneNumbers', default_factory=random_phone)
    reserve: bool = Field(default_factory=random_bool)
    # team_id: str = Field(default_factory=random_id)
    university_course: str = Field(alias='universityCourse', default_factory=random_course)
    university_faculty: str = Field(alias='universityFaculty', default_factory=random_string)


class DefaultParticipant(BaseModel):
    id: str = Field(default_factory=random_id)
    coach: bool = Field(default_factory=random_bool)
    contact: bool = Field(default_factory=random_bool)
    email_address: str = Field(alias='emailAdress', default_factory=random_email)
    # event_id
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    main: bool = Field(default_factory=random_bool)
    name: str = Field(default_factory=random_string)
    organization: str = Field(default_factory=random_string)
    phone_numbers: str = Field(alias='phoneNumbers', default_factory=random_phone)
    reserve: bool = Field(default_factory=random_bool)
    # team_id: str = Field(default_factory=random_id)
    university_course: str = Field(alias='universityCourse', default_factory=random_course)
    university_faculty: str = Field(alias='universityFaculty', default_factory=random_string)


class DefaultParticipantsList(BaseModel):
    Items: list[DefaultParticipant]
    CountList: int


class ParticipantDict(TypedDict):
    id: str
    coach: bool
    contact: bool
    email_address: str
    # event_id
    forSorted: int
    main: bool
    name: str
    organization: str
    phone_numbers: str
    reserve: bool
    # team_id: str = Field(default_factory=random_id)
    university_course: str
    university_faculty: str
