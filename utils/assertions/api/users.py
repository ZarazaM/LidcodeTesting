# TODO заполнить
from models.users import DefaultUser, UserDict, UpdateUser
from utils.assertions.base.expect import expect


def assert_user(
        expected_user: UserDict,
        actual_user: DefaultUser | UpdateUser
):
    pass
