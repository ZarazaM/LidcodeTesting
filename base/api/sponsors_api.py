import allure
from httpx import Response

from base.client import get_client
from models.sponsors import DefaultSponsor, UpdateSponsor
from utils.constants.routes import APIRoutes
from models.authentication import Authentication


@allure.step(f'Getting all sponsors')
def get_sponsors_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.SPONSORS, timeout=10)


@allure.step('Getting sponsors with id "{sponsor_id}"')
def get_sponsor_api(
        sponsor_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {'id': sponsor_id}
    return client.get(f'{APIRoutes.SPONSORS}', params=params, timeout=10)


@allure.step('Creating sponsor')
def create_sponsor_api(
        payload: DefaultSponsor,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.SPONSORS, json={"Items": [payload.dict(by_alias=True)]}, timeout=10)


@allure.step('Updating sponsor with id "{sponsor_id}"')
def update_sponsor_api(
        sponsor_id: str,
        payload: UpdateSponsor,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    payload_dict = payload.dict(by_alias=True)
    payload_dict['id'] = sponsor_id
    return client.put(f'{APIRoutes.SPONSORS}', json={"Items": [payload_dict]}, timeout=10)


@allure.step('Deleting sponsor with id "{sponsor_id}"')
def delete_sponsor_api(
        sponsor_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {"id": sponsor_id}
    return client.delete(f'{APIRoutes.SPONSORS}', params=params, timeout=10)


def create_sponsor(auth: Authentication = Authentication()) -> DefaultSponsor:
    payload = DefaultSponsor()

    response = create_sponsor_api(payload=payload, auth=auth)
    # del response.json()['Items'][0]['imageDef']
    # del response.json()['Items'][0]['imageHor']
    # del response.json()['Items'][0]['imageVer']
    return DefaultSponsor(**response.json()['Items'][0])
