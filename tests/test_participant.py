from http import HTTPStatus

import allure
import pytest

from base.api.participants_api import (create_participant_api, delete_participant_api,
                                       get_participant_api, get_participants_api, update_participant_api)
from models.participants import (DefaultParticipant, DefaultParticipantsList, ParticipantDict, UpdateParticipant)

from utils.assertions.api.participants import assert_participant
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.participants
@allure.feature('Participants')
@allure.story('Participants API')
class TestParticipants:
    @allure.title('Get participants')
    def test_get_participants(self):
        response = get_participants_api()

        json_response: ParticipantDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultParticipantsList.schema())

    @allure.title('Create participant')
    def test_create_participant(self):
        payload = DefaultParticipant()

        response = create_participant_api(payload=payload)
        json_response: ParticipantDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_participant(
            expected_participant=json_response,
            actual_participant=payload
        )

        validate_schema(json_response, DefaultParticipant.schema())

        delete_participant_api(json_response['Items'][0]['id'])

    @allure.title('Get participant')
    def test_get_participant(self, function_participant: DefaultParticipant):
        response = get_participant_api(function_participant.id)

        json_response: ParticipantDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_participant(
            expected_participant=json_response,
            actual_participant=function_participant
        )

        validate_schema(json_response, DefaultParticipant.schema())

    @allure.title('Update participant')
    def test_update_participant(self, function_participant: DefaultParticipant):
        payload = UpdateParticipant()

        response = update_participant_api(function_participant.id, payload=payload)
        json_response: ParticipantDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_participant(
            expected_participant=json_response,
            actual_participant=payload
        )

        validate_schema(json_response, DefaultParticipant.schema())

    @allure.title('Delete participant')
    def test_delete_participant(self, function_participant: DefaultParticipant):
        delete_participant_response = delete_participant_api(function_participant.id)
        json_delete_participant_response: ParticipantDict = delete_participant_response.json()

        get_participant_response = get_participant_api(function_participant.id)

        assert_status_code(delete_participant_response.status_code, HTTPStatus.OK)
        assert_status_code(get_participant_response.status_code, HTTPStatus.OK)

        assert_participant(
            expected_participant=json_delete_participant_response,
            actual_participant=function_participant
        )

        validate_schema(json_delete_participant_response, DefaultParticipant.schema())

        assert get_participant_response.json()['CountList'] == 0
