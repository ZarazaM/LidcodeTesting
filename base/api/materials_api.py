import allure
from httpx import Response

from base.client import get_client
from models.materials import DefaultMaterial, UpdateMaterial
from utils.constants.routes import APIRoutes
from models.authentication import Authentication


@allure.step(f'Getting all materials')
def get_materials_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.MATERIALS, timeout=10)


@allure.step('Getting materials with id "{material_id}"')
def get_material_api(
        material_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {'id': material_id}
    return client.get(f'{APIRoutes.MATERIALS}', params=params, timeout=10)


@allure.step('Creating material')
def create_material_api(
        payload: DefaultMaterial,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.MATERIALS, json={"Items": [payload.dict(by_alias=True)]}, timeout=10)


@allure.step('Updating material with id "{material_id}"')
def update_material_api(
        material_id: str,
        payload: UpdateMaterial,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    payload_dict = payload.dict(by_alias=True)
    payload_dict['id'] = material_id
    return client.put(f'{APIRoutes.MATERIALS}', json={"Items": [payload_dict]}, timeout=10)


@allure.step('Deleting material with id "{material_id}"')
def delete_material_api(
        material_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {"id": material_id}
    return client.delete(f'{APIRoutes.MATERIALS}', params=params, timeout=10)


def create_material(auth: Authentication = Authentication()) -> DefaultMaterial:
    payload = DefaultMaterial()

    response = create_material_api(payload=payload, auth=auth)

    return DefaultMaterial(**response.json()['Items'][0])
