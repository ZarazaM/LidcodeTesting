from http import HTTPStatus

import allure
import pytest

from base.api.users_api import (create_user_api, delete_user_api, get_user_api, get_users_api, update_user_api)
from models.users import (DefaultUser, DefaultUsersList, UserDict, UpdateUser)

from utils.assertions.api.users import assert_user
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.users
@allure.feature('Users')
@allure.story('Users API')
class TestUsers:
    @allure.title('Get users')
    def test_get_users(self):
        response = get_users_api()
        json_response: UserDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultUsersList.schema())

    @allure.title('Create user')
    def test_create_user(self):
        payload = DefaultUser()

        response = create_user_api(payload=payload)
        json_response: UserDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_user(
            expected_user=json_response,
            actual_user=payload
        )

        validate_schema(json_response, DefaultUser.schema())

        delete_user_api(json_response['Items'][0]['id'])

    @allure.title('Get user')
    def test_get_user(self, function_user: DefaultUser):
        response = get_user_api(function_user.id)
        json_response: UserDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_user(
            expected_user=json_response,
            actual_user=function_user
        )

        validate_schema(json_response, DefaultUser.schema())

    @allure.title('Update user')
    def test_update_user(self, function_user: DefaultUser):
        payload = UpdateUser()

        response = update_user_api(function_user.id, payload=payload)
        json_response: UserDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_user(
            expected_user=json_response,
            actual_user=payload
        )

        validate_schema(json_response, DefaultUser.schema())

    @allure.title('Delete user')
    def test_delete_user(self, function_user: DefaultUser):
        delete_user_response = delete_user_api(function_user.id)
        json_delete_user_response: UserDict = delete_user_response.json()

        get_user_response = get_user_api(function_user.id)

        assert_status_code(delete_user_response.status_code, HTTPStatus.OK)
        assert_status_code(get_user_response.status_code, HTTPStatus.OK)

        assert_user(
            expected_user=json_delete_user_response,
            actual_user=function_user
        )

        validate_schema(json_delete_user_response, DefaultUser.schema())

        assert get_user_response.json()['CountList'] == 0
