import time
from dm_api_account.models.user_envelope import Roles
from services import *
from dm_api_account.models import *
from hamcrest import assert_that, has_properties


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    login = "Cat30"
    password = "meowmeow"
    email = "Kitty_cat30@gmail.com"

    json_account = Registration(
        login=login,
        email=email,
        password=password
    )
    api.account.post_v1_account(json=json_account)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)

    json = ResetPassword(
        login=login,
        email=email
    )
    response = api.account.post_v1_account_password(json=json)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))