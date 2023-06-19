import allure
from httpx import Response

from base.client import get_client
from models.users import DefaultUser, UpdateUser
from utils.constants.routes import APIRoutes
from models.authentication import Authentication


@allure.step(f'Getting all users')
def get_users_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.USERS, timeout=10)


@allure.step('Getting users with id "{user_id}"')
def get_user_api(
        user_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {'id': user_id}
    return client.get(f'{APIRoutes.USERS}', params=params, timeout=10)


@allure.step('Creating user')
def create_user_api(
        payload: DefaultUser,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.USERS, json={"Items": [payload.dict(by_alias=True)]}, timeout=10)


@allure.step('Updating user with id "{user_id}"')
def update_user_api(
        user_id: str,
        payload: UpdateUser,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    payload_dict = payload.dict(by_alias=True)
    payload_dict['id'] = user_id
    return client.put(f'{APIRoutes.USERS}', json={"Items": [payload_dict]}, timeout=10)


@allure.step('Deleting user with id "{user_id}"')
def delete_user_api(
        user_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {"id": user_id}
    return client.delete(f'{APIRoutes.USERS}', params=params, timeout=10)


def create_user(auth: Authentication = Authentication()) -> DefaultUser:
    payload = DefaultUser()

    response = create_user_api(payload=payload, auth=auth)

    return DefaultUser(**response.json()['Items'][0])
