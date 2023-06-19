from functools import lru_cache

from httpx import Client, Response

from models.authentication import AuthUser
from settings import base_settings
from utils.constants.routes import APIRoutes
from http import HTTPStatus


def get_auth_token_api(payload: AuthUser) -> Response:
    client = Client(base_url=base_settings.api_url)
    return client.post(f'{APIRoutes.GET_TOKEN}', json=payload.dict(), timeout=10)


def get_auth_token(payload: AuthUser) -> str:

    response = get_auth_token_api(payload)
    json_response = response.json()

    response.status_code = HTTPStatus.OK

    return json_response['token']
