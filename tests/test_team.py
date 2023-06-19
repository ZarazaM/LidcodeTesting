from http import HTTPStatus

import allure
import pytest

from base.api.teams_api import (create_team_api, delete_team_api, get_team_api, get_teams_api, update_team_api)
from models.teams import (DefaultTeam, DefaultTeamsList, TeamDict, UpdateTeam)
from models.participants import DefaultParticipant

from utils.assertions.api.teams import assert_team
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.teams
@allure.feature('Teams')
@allure.story('Teams API')
class TestTeams:
    @allure.title('Get teams')
    def test_get_teams(self):
        response = get_teams_api()
        json_response: TeamDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultTeamsList.schema())

    @allure.title('Create team')
    def test_create_team(self):
        payload = DefaultTeam()

        response = create_team_api(payload=payload)
        json_response: TeamDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_team(
            expected_team=json_response,
            actual_team=payload
        )

        validate_schema(json_response, DefaultTeam.schema())

        delete_team_api(json_response['TeamData'][0]['id'])

    @allure.title('Get team')
    def test_get_team(self, function_team: DefaultTeam):
        response = get_team_api(function_team.id)
        json_response: TeamDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_team(
            expected_team=json_response,
            actual_team=function_team
        )

        validate_schema(json_response, DefaultTeam.schema())

    @allure.title('Update team')
    def test_update_team(self, function_team: DefaultTeam):
        payload = UpdateTeam()

        response = update_team_api(function_team.id, payload=payload)
        json_response: TeamDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_team(
            expected_team=json_response,
            actual_team=payload
        )

        validate_schema(json_response, DefaultTeam.schema())

    @allure.title('Delete team')
    def test_delete_team(self, function_team: DefaultTeam):
        delete_team_response = delete_team_api(function_team.id)
        json_delete_team_response: TeamDict = delete_team_response.json()

        get_team_response = get_team_api(function_team.id)

        assert_status_code(delete_team_response.status_code, HTTPStatus.OK)
        assert_status_code(get_team_response.status_code, HTTPStatus.OK)

        assert_team(
            expected_team=json_delete_team_response,
            actual_team=function_team
        )

        validate_schema(json_delete_team_response, DefaultTeam.schema())
