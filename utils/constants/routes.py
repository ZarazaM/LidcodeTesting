from enum import Enum


class APIRoutes(str, Enum):
    PARTICIPANTS = 'participants/'
    EVENTS = 'events/'
    TEAMS = 'teams/'
    SPONSORS = 'sponsors/'
    ORGANIZERS = 'organizers/'
    MATERIALS = 'materials/'
    USERS = 'users/'
    EVENT_MATERIAL = 'event_material/'
    EVENT_ORGANIZER = 'event_organizer/'
    EVENT_SPONSOR = 'event_sponsor/'
    EVENTS_ON_MAIN_LIST = 'events_on_main_list/'
    EVENT_INFO_ALL = 'event_info_all/'
    EVENT_INFO_REGULATIONS = 'event_info_regulations/'
    EVENT_CHECK_REGISTRATION = 'event_check_registration/'
    TEAM_REGISTRATION = 'team_registration/'
    GET_TOKEN = 'user_login/'

    def __str__(self) -> str:
        return self.value
