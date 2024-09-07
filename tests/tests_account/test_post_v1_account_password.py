from apis.dm_api_account.models import *
from hamcrest import assert_that, has_properties


def test_post_v1_account_password(
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
    dm_api_facade.account.activate_registered_user(login=login)
    response = dm_api_facade.account.reset_registered_password(
        login=login,
        email=email
    )
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))
