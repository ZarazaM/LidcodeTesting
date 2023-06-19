import allure
from httpx import Response

from base.client import get_client
from models.events import DefaultEvent, UpdateEvent
from utils.constants.routes import APIRoutes
from models.authentication import Authentication


@allure.step(f'Getting all events')
def get_events_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.EVENTS, timeout=10)


@allure.step('Getting events with id "{event_id}"')
def get_event_api(
        event_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {'id': event_id}
    return client.get(f'{APIRoutes.EVENTS}', params=params, timeout=10)


@allure.step('Creating event')
def create_event_api(
        payload: DefaultEvent,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    print(payload.dict(by_alias=True))
    return client.post(APIRoutes.EVENTS, json={"EventData": payload.dict(by_alias=True)}, timeout=10)


@allure.step('Updating event with id "{event_id}"')
def update_event_api(
        event_id: str,
        payload: UpdateEvent,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    payload_dict = payload.dict(by_alias=True)
    payload_dict['id'] = event_id
    return client.put(f'{APIRoutes.EVENTS}', json={"EventData": payload_dict,
                                                   "OrganizersList": [], "SponsorsList": [],
                                                   "MaterialsList": [], "TeamsList": []}, timeout=10)


@allure.step('Deleting event with id "{event_id}"')
def delete_event_api(
        event_id: str,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    params = {"id": event_id}
    return client.delete(f'{APIRoutes.EVENTS}', params=params, timeout=10)


def create_event(auth: Authentication = Authentication()) -> DefaultEvent:
    payload = DefaultEvent()
    print('payload', payload.dict(by_alias=True))
    response = create_event_api(payload=payload, auth=auth)
    print('resp', response.json())
    return DefaultEvent(**response.json()['Items'][0])
