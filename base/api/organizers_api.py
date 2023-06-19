import allure
from httpx import Response

from base.client import get_client
from models.organizers import DefaultOrganizer, UpdateOrganizer
from utils.constants.routes import APIRoutes
from models.authentication import Authentication


@allure.step(f'Getting all organizers')
def get_organizers_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.ORGANIZERS, timeout=10)


@allure.step('Getting organizers with id "{organizer_id}"')
def get_organizer_api(
        organizer_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {'id': organizer_id}
    return client.get(f'{APIRoutes.ORGANIZERS}', params=params, timeout=10)


@allure.step('Creating organizer')
def create_organizer_api(
        payload: DefaultOrganizer,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.ORGANIZERS, json={"Items": [payload.dict(by_alias=True)]}, timeout=10)


@allure.step('Updating organizer with id "{organizer_id}"')
def update_organizer_api(
        organizer_id: str,
        payload: UpdateOrganizer,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    payload_dict = payload.dict(by_alias=True)
    payload_dict['id'] = organizer_id
    return client.put(f'{APIRoutes.ORGANIZERS}', json={"Items": [payload_dict]}, timeout=10)


@allure.step('Deleting organizer with id "{organizer_id}"')
def delete_organizer_api(
        organizer_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {"id": organizer_id}
    return client.delete(f'{APIRoutes.ORGANIZERS}', params=params, timeout=10)


def create_organizer(auth: Authentication = Authentication()) -> DefaultOrganizer:
    payload = DefaultOrganizer()

    response = create_organizer_api(payload=payload, auth=auth)

    return DefaultOrganizer(**response.json()['Items'][0])
