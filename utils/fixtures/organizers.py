import pytest

from base.api.organizers_api import create_organizer, delete_organizer_api
from models.organizers import DefaultOrganizer


@pytest.fixture(scope='function')
def function_organizer() -> DefaultOrganizer:
    organizer = create_organizer()
    yield organizer

    delete_organizer_api(organizer.id)
