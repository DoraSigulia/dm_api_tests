from hamcrest import assert_that, has_properties
from apis.dm_api_account.models import *


def test_put_v1_account_password(
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
    new_password = "123user"
    dm_api_facade.account.activate_registered_user(login=login)
    dm_api_facade.account.reset_registered_password(
        login=login,
        email=email
    )
    headers = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.set_headers(headers=headers)

    response_password = dm_api_facade.account.change_registered_password(
        login=login,
        old_password=password,
        new_password=new_password)

    assert_that(response_password.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))
    assert_that(response_password.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))
