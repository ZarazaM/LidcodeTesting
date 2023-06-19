import pytest

from base.api.users_api import create_user, delete_user_api
from models.users import DefaultUser


@pytest.fixture(scope='function')
def function_user() -> DefaultUser:
    user = create_user()
    yield user

    delete_user_api(user.id)
