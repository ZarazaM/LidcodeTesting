# TODO заполнить
from models.organizers import DefaultOrganizer, OrganizerDict, UpdateOrganizer
from utils.assertions.base.expect import expect


def assert_organizer(
        expected_organizer: OrganizerDict,
        actual_organizer: DefaultOrganizer | UpdateOrganizer
):
    pass
