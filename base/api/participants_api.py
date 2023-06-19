import allure
from httpx import Response

from base.client import get_client
from models.participants import DefaultParticipant, UpdateParticipant
from utils.constants.routes import APIRoutes
from models.authentication import Authentication


@allure.step(f'Getting all participants')
def get_participants_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.PARTICIPANTS, timeout=30)


@allure.step('Getting participants with id "{participant_id}"')
def get_participant_api(
        participant_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {'id': participant_id}
    return client.get(f'{APIRoutes.PARTICIPANTS}', params=params, timeout=30)


@allure.step('Creating participant')
def create_participant_api(
        payload: DefaultParticipant,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.PARTICIPANTS, json={"Items": [payload.dict(by_alias=True)]}, timeout=10)


@allure.step('Updating participant with id "{participant_id}"')
def update_participant_api(
        participant_id: str,
        payload: UpdateParticipant,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    payload_dict = payload.dict(by_alias=True)
    payload_dict['id'] = participant_id
    return client.put(f'{APIRoutes.PARTICIPANTS}', json={"Items": [payload_dict]}, timeout=10)


@allure.step('Deleting participant with id "{participant_id}"')
def delete_participant_api(
        participant_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {"id": participant_id}
    return client.delete(f'{APIRoutes.PARTICIPANTS}', params=params, timeout=10)


def create_participant(auth: Authentication = Authentication()) -> DefaultParticipant:
    payload = DefaultParticipant()

    response = create_participant_api(payload=payload, auth=auth)

    return DefaultParticipant(**response.json()['Items'][0])
