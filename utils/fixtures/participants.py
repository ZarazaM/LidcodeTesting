import pytest

from base.api.participants_api import create_participant, delete_participant_api
from models.participants import DefaultParticipant


@pytest.fixture(scope='function')
def function_participant() -> DefaultParticipant:
    participant = create_participant()

    yield participant

    delete_participant_api(participant.id)
