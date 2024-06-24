import time
from services import *
from dm_api_account.models import *
from dm_api_account.models.user_envelope import Roles
from hamcrest import assert_that, has_properties


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "Cat002"
    json = Registration(
        login=login,
        email="Kitty_cat002@gmail.com",
        password="meowmeow"
    )
    api.account.post_v1_account(json=json, status_code=201)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response_token = api.account.put_v1_account_token(token=token)
    assert_that(response_token.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))

