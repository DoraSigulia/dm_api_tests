from dm_api_account.models.user_envelope import Roles
from services import *
from hamcrest import assert_that, has_properties


def test_post_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    login = "Fox11"
    email = "Fox11@gmail.com"
    old_password = "gavgav1"

    api.account.register_new_user(
        login=login,
        email=email,
        password=old_password
    )
    api.account.activate_registered_user(login=login)
    response = api.account.reset_registered_password(
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
