from services import *
from dm_api_account.models.user_envelope import Roles
from hamcrest import assert_that, has_properties


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "Cat83"
    email = "Kitty83@gmail.com"
    password = "meowmeow"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    response_token = api.account.activate_registered_user(login=login)
    assert_that(response_token.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))
