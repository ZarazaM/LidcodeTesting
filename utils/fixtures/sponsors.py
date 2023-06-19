import pytest

from base.api.sponsors_api import create_sponsor, delete_sponsor_api
from models.sponsors import DefaultSponsor


@pytest.fixture(scope='function')
def function_sponsor() -> DefaultSponsor:
    sponsor = create_sponsor()
    yield sponsor

    delete_sponsor_api(sponsor.id)
