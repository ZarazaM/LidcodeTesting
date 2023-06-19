from http import HTTPStatus

import allure
import pytest

from base.api.events_api import (create_event_api, delete_event_api, get_event_api, get_events_api, update_event_api)
from models.events import (DefaultEvent, DefaultEventsList, EventDict, UpdateEvent)

from utils.assertions.api.events import assert_event
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.events
@allure.feature('Events')
@allure.story('Events API')
class TestEvents:
    @allure.title('Get events')
    def test_get_events(self):
        response = get_events_api()
        json_response: EventDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultEventsList.schema())

    @allure.title('Create event')
    def test_create_event(self):
        payload = DefaultEvent()

        response = create_event_api(payload=payload)
        json_response: EventDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_event(
            expected_event=json_response,
            actual_event=payload
        )

        validate_schema(json_response, DefaultEvent.schema())

        delete_event_api(json_response['Items'][0]['id'])

    @allure.title('Get event')
    def test_get_event(self, function_event: DefaultEvent):
        response = get_event_api(function_event.id)
        json_response: EventDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_event(
            expected_event=json_response,
            actual_event=function_event
        )

        validate_schema(json_response, DefaultEvent.schema())

    @allure.title('Update event')
    def test_update_event(self, function_event: DefaultEvent):
        payload = UpdateEvent()

        response = update_event_api(function_event.id, payload=payload)
        json_response: EventDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_event(
            expected_event=json_response,
            actual_event=payload
        )

        validate_schema(json_response, DefaultEvent.schema())

    @allure.title('Delete event')
    def test_delete_event(self, function_event: DefaultEvent):
        delete_event_response = delete_event_api(function_event.id)
        json_delete_event_response: EventDict = delete_event_response.json()

        get_event_response = get_event_api(function_event.id)

        assert_status_code(delete_event_response.status_code, HTTPStatus.OK)
        assert_status_code(get_event_response.status_code, HTTPStatus.OK)

        assert_event(
            expected_event=json_delete_event_response,
            actual_event=function_event
        )

        validate_schema(json_delete_event_response, DefaultEvent.schema())
