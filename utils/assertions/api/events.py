# TODO заполнить
from models.events import DefaultEvent, EventDict, UpdateEvent
from utils.assertions.base.expect import expect


def assert_event(
        expected_event: EventDict,
        actual_event: DefaultEvent | UpdateEvent
):
    pass