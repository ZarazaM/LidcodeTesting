from typing import TypedDict

from pydantic import BaseModel, Field

from utils.fakers import random_string, random_number, random_id, random_datetime, random_event_status, random_bool


class UpdateEvent(BaseModel):
    date_close_register: str = Field(alias='dateCloseRegister', default_factory=random_datetime)
    date_end: str = Field(alias='dateEnd', default_factory=random_datetime)
    date_register: str = Field(alias='dateRegister', default_factory=random_datetime)
    date_start: str = Field(alias='dateStart', default_factory=random_datetime)
    time_publication_additional_material: str = Field(alias='timePublicationAdditionalMaterial', default_factory=random_datetime)
    description: str = Field(default_factory=random_string)
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    # imageDef:
    # imageHor:
    # imageVer:
    max_number_of_participants: int = Field(alias='maxNumberOfParticipants', default_factory=random_number)
    max_number_of_team: int = Field(alias='maxNumberOfTeam', default_factory=random_number)
    min_number_of_participants: int = Field(alias='minNumberOfParticipants', default_factory=random_number)
    name: str = Field(default_factory=random_string)
    regulations: str = Field(default_factory=random_string)
    # results:
    status: str = Field(default_factory=random_event_status)
    # status_now:
    #status_materials: bool = Field(alias='statusMaterials', default_factory=random_bool)


class DefaultEvent(BaseModel):
    id: str = Field(default_factory=random_id)
    date_close_register: str = Field(alias='dateCloseRegister', default_factory=random_datetime)
    date_end: str = Field(alias='dateEnd', default_factory=random_datetime)
    date_register: str = Field(alias='dateRegister', default_factory=random_datetime)
    date_start: str = Field(alias='dateStart', default_factory=random_datetime)
    time_publication_additional_material: str = Field(alias='timePublicationAdditionalMaterial', default_factory=random_datetime)
    description: str = Field(default_factory=random_string)
    for_sorted: int = Field(alias='forSorted', default_factory=random_number)
    # imageDef:
    # imageHor:
    # imageVer:
    max_number_of_participants: int = Field(alias='maxNumberOfParticipants', default_factory=random_number)
    max_number_of_team: int = Field(alias='maxNumberOfTeam', default_factory=random_number)
    min_number_of_participants: int = Field(alias='minNumberOfParticipants', default_factory=random_number)
    name: str = Field(default_factory=random_string)
    regulations: str = Field(default_factory=random_string)
    # results:
    status: str = Field(default_factory=random_event_status)
    # status_now:
    #status_materials: bool = Field(alias='statusMaterials', default_factory=random_bool)


class DefaultEventsList(BaseModel):
    Items: list[DefaultEvent]
    CountList: int


class EventDict(TypedDict):
    id: str
    dateCloseRegister: str
    dateEnd: str
    dateRegister: str
    dateStart: str
    timePublicationAdditionalMaterial: str
    description: str
    forSorted: int
    # imageDef:
    # imageHor:
    # imageVer:
    maxNumberOfParticipants: int
    maxNumberOfTeam: int
    minNumberOfParticipants: int
    name: str
    regulations: str
    # results:
    status: str
    # status_now:
    #statusMaterials: bool
