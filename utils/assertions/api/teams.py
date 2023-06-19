# TODO заполнить
from models.teams import DefaultTeam, TeamDict, UpdateTeam
from utils.assertions.base.expect import expect


def assert_team(
        expected_team: TeamDict,
        actual_team: DefaultTeam | UpdateTeam
):
    pass
