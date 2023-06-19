from http import HTTPStatus

import allure
import pytest

from base.api.organizers_api import (create_organizer_api, delete_organizer_api,
                                     get_organizer_api, get_organizers_api, update_organizer_api)
from models.organizers import (DefaultOrganizer, DefaultOrganizersList, OrganizerDict, UpdateOrganizer)

from utils.assertions.api.organizers import assert_organizer
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.organizers
@allure.feature('Organizers')
@allure.story('Organizers API')
class TestOrganizers:
    @allure.title('Get organizers')
    def test_get_organizers(self):
        response = get_organizers_api()
        json_response: OrganizerDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultOrganizersList.schema())

    @allure.title('Create organizer')
    def test_create_organizer(self):
        payload = DefaultOrganizer()

        response = create_organizer_api(payload=payload)
        json_response: OrganizerDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_organizer(
            expected_organizer=json_response,
            actual_organizer=payload
        )

        validate_schema(json_response, DefaultOrganizer.schema())

        delete_organizer_api(json_response['Items'][0]['id'])

    @allure.title('Get organizer')
    def test_get_organizer(self, function_organizer: DefaultOrganizer):
        response = get_organizer_api(function_organizer.id)
        json_response: OrganizerDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_organizer(
            expected_organizer=json_response,
            actual_organizer=function_organizer
        )

        validate_schema(json_response, DefaultOrganizer.schema())

    @allure.title('Update organizer')
    def test_update_organizer(self, function_organizer: DefaultOrganizer):
        payload = UpdateOrganizer()

        response = update_organizer_api(function_organizer.id, payload=payload)
        json_response: OrganizerDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_organizer(
            expected_organizer=json_response,
            actual_organizer=payload
        )

        validate_schema(json_response, DefaultOrganizer.schema())

    @allure.title('Delete organizer')
    def test_delete_organizer(self, function_organizer: DefaultOrganizer):
        delete_organizer_response = delete_organizer_api(function_organizer.id)
        json_delete_organizer_response: OrganizerDict = delete_organizer_response.json()

        get_organizer_response = get_organizer_api(function_organizer.id)

        assert_status_code(delete_organizer_response.status_code, HTTPStatus.OK)
        assert_status_code(get_organizer_response.status_code, HTTPStatus.OK)

        assert_organizer(
            expected_organizer=json_delete_organizer_response,
            actual_organizer=function_organizer
        )

        validate_schema(json_delete_organizer_response, DefaultOrganizer.schema())

        assert get_organizer_response.json()['CountList'] == 0
