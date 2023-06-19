import pytest

from base.api.teams_api import create_team, delete_team_api
from base.api.participants_api import create_participant, delete_participant_api
from models.teams import DefaultTeam


@pytest.fixture(scope='function')
def function_team() -> DefaultTeam:
    team = create_team()
    yield team

    delete_team_api(team.id)
