import allure
from httpx import Response

from base.client import get_client
from models.teams import DefaultTeam, UpdateTeam
from models.participants import DefaultParticipant
from utils.constants.routes import APIRoutes
from models.authentication import Authentication


@allure.step(f'Getting all teams')
def get_teams_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.TEAMS, timeout=10)


@allure.step('Getting teams with id "{team_id}"')
def get_team_api(
        team_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {'id': team_id}
    return client.get(f'{APIRoutes.TEAMS}', params=params, timeout=10)


@allure.step('Creating team')
def create_team_api(
        payload: DefaultTeam,
        participant_payload: DefaultParticipant = DefaultParticipant(),
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.TEAMS,
                       json={"TeamData": payload.dict(by_alias=True),
                             "TeamListParticipantsData": [participant_payload.dict(by_alias=True)]}, timeout=10)


@allure.step('Updating team with id "{team_id}"')
def update_team_api(
        team_id: str,
        payload: UpdateTeam,
        participant_payload: DefaultParticipant = DefaultParticipant(),
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    payload_dict = payload.dict(by_alias=True)
    payload_dict['id'] = team_id
    return client.put(f'{APIRoutes.TEAMS}',
                      json={"TeamData": payload_dict,
                            "TeamListParticipantsData": [participant_payload.dict(by_alias=True)]}, timeout=10)


@allure.step('Deleting team with id "{team_id}"')
def delete_team_api(
        team_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {"id": team_id}
    return client.delete(f'{APIRoutes.TEAMS}', params=params, timeout=10)


def create_team(auth: Authentication = Authentication()) -> DefaultTeam:
    payload = DefaultTeam()
    participant_payload = DefaultParticipant()

    response = create_team_api(payload=payload, participant_payload=participant_payload, auth=auth)

    return DefaultTeam(**response.json()['TeamData'][0])
