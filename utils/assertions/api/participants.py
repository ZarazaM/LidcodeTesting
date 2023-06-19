# TODO заполнить
from models.participants import DefaultParticipant, ParticipantDict, UpdateParticipant
from utils.assertions.base.expect import expect


def assert_participant(
        expected_participant: ParticipantDict,
        actual_participant: DefaultParticipant | UpdateParticipant
):
    pass