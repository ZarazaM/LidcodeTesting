from http import HTTPStatus

import allure
import pytest

from base.api.sponsors_api import (create_sponsor_api, delete_sponsor_api,
                                   get_sponsor_api, get_sponsors_api, update_sponsor_api)
from models.sponsors import (DefaultSponsor, DefaultSponsorsList, SponsorDict, UpdateSponsor)

from utils.assertions.api.sponsors import assert_sponsor
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.sponsors
@allure.feature('Sponsors')
@allure.story('Sponsors API')
class TestSponsors:
    @allure.title('Get sponsors')
    def test_get_sponsors(self):
        response = get_sponsors_api()
        json_response: SponsorDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultSponsorsList.schema())

    @allure.title('Create sponsor')
    def test_create_sponsor(self):
        payload = DefaultSponsor()

        response = create_sponsor_api(payload)
        json_response: SponsorDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_sponsor(
            expected_sponsor=json_response,
            actual_sponsor=payload
        )

        validate_schema(json_response, DefaultSponsor.schema())

        delete_sponsor_api(json_response['Items'][0]['id'])

    @allure.title('Get sponsor')
    def test_get_sponsor(self, function_sponsor: DefaultSponsor):
        response = get_sponsor_api(function_sponsor.id)
        json_response: SponsorDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_sponsor(
            expected_sponsor=json_response,
            actual_sponsor=function_sponsor
        )

        validate_schema(json_response, DefaultSponsor.schema())

    @allure.title('Update sponsor')
    def test_update_sponsor(self, function_sponsor: DefaultSponsor):
        payload = UpdateSponsor()

        response = update_sponsor_api(function_sponsor.id, payload)
        json_response: SponsorDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_sponsor(
            expected_sponsor=json_response,
            actual_sponsor=payload
        )

        validate_schema(json_response, DefaultSponsor.schema())

    @allure.title('Delete sponsor')
    def test_delete_sponsor(self, function_sponsor: DefaultSponsor):

        delete_sponsor_response = delete_sponsor_api(function_sponsor.id)
        json_delete_sponsor_response: SponsorDict = delete_sponsor_response.json()

        get_sponsor_response = get_sponsor_api(function_sponsor.id)

        assert_status_code(delete_sponsor_response.status_code, HTTPStatus.OK)
        assert_status_code(get_sponsor_response.status_code, HTTPStatus.OK)

        assert_sponsor(
            expected_sponsor=json_delete_sponsor_response,
            actual_sponsor=function_sponsor
        )

        validate_schema(json_delete_sponsor_response, DefaultSponsor.schema())

        assert get_sponsor_response.json()['CountList'] == 0
