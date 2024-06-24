import time
from services import *
from dm_api_account.models import *
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import Roles


def test_put_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    login = "Cat__"
    email = "Kitty_cat__@gmail.com"
    old_password = "meowmeow1"
    new_password = "meowmeow2"

    json_account = Registration(
        login=login,
        email=email,
        password=old_password
    )
    api.account.post_v1_account(json=json_account)
    time.sleep(2)
    token_create = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token_create)

    json = ResetPassword(
        login=login,
        email=email
    )
    api.account.post_v1_account_password(json=json)
    time.sleep(2)
    token_reset = mailhog.get_token_from_last_email_by_name(login=login) # '82c1996e-84fb-40d8-b58c-80192dc2bbe'

    json = ChangePassword(
        login=login,
        token=token_reset,
        oldPassword=old_password,
        newPassword=new_password
    )
    response_password = api.account.put_v1_account_password(json=json)
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
