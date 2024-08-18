import time
import pytest
from generic.helpers.orm_models import User
from hamcrest import assert_that, has_properties, has_entries
from dm_api_account.models.user_envelope import Roles
from string import ascii_letters, digits
import random


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


def test_post_v1_account(
        mailhog,
        dm_api_facade,
        orm,
        prepare_user
):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    status_code = prepare_user.status_code
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    dataset = orm.get_user_by_user(login=login)
    row: User
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': False
            }
        ))
    response_token = dm_api_facade.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset2 = orm.get_user_by_user(login=login)
    for row in dataset2:
        assert_that(row, has_entries(
            {
                'Activated': True
            }
        ))

    assert_that(response_token.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))



@pytest.mark.parametrize('login, email, password, status_code, check', [
    ('User', 'user@mail.ru', 'user123', 201, ''),
    ('User', 'user@mail.ru', random_string(1, 1), 400, {'Password': ['Short']}),
    ('User', 'user@mail.ru', random_string(1000, 1000), 201, ''),
    (random_string(1, 1), random_string(5, 6) + '@mail.ru', random_string(6, 10), 400, {'Login': ['Short']}),
    ('', random_string(5, 6) + '@mail.ru', random_string(6, 10), 400, {'Login': ['Empty', 'Short']}),
    (random_string(1000, 1000), random_string(5, 6) + '@mail.ru', random_string(6, 10), 400, {'Login': ['Long']}),
    ('User', '@mail.ru', random_string(6, 10), 400, {'Email': ['Invalid']}),
    ('User', random_string(6, 10), random_string(6, 10), 400, {'Email': ['Invalid']}),
])
def test_post_v1_account_with_diff_params(
        mailhog,
        dm_api_facade,
        orm,
        login,
        email,
        password,
        status_code,
        check
):
    login = login
    email = email
    password = password
    status_code = status_code
    orm.delete_user_by_login(login=login)
    dm_api_facade.mailhog.delete_message_by_login(login=login)
    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    if status_code == 201:
        dataset = orm.get_user_by_user(login=login)
        row: User
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': False
                }
            ))
        response_token = dm_api_facade.account.activate_registered_user(login=login)
        time.sleep(2)
        dataset2 = orm.get_user_by_user(login=login)
        for row in dataset2:
            assert_that(row, has_entries(
                {
                    'Activated': True
                }
            ))

        assert_that(response_token.resource, has_properties(
            {
                "login": login,
                "roles": [Roles.GUEST, Roles.PLAYER],
                "medium_picture_url": None
            }
        ))

    else:
        assert_that(response.json(), has_entries(
            {
                'errors': check
            }
        ))
