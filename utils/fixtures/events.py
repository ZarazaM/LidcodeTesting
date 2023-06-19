import pytest

from base.api.events_api import create_event, delete_event_api
from models.events import DefaultEvent


@pytest.fixture(scope='function')
def function_event() -> DefaultEvent:
    event = create_event()
    yield event

    delete_event_api(event.id)
