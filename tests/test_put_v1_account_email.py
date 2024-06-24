import time
from services import *
from dm_api_account.models import *
from hamcrest import assert_that, has_properties


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "Cat41"
    password = "meowmeow"
    old_email = "Kitty_cat41@gmail.com"
    new_email = "Kitty_cat51@gmail.com"

    json_account = Registration(
        login=login,
        email=old_email,
        password=password
    )
    api.account.post_v1_account(json=json_account)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)

    json_email = ChangeEmail(
        login=login,
        password=password,
        email=new_email
    )
    response_email = api.account.put_v1_account_email(json=json_email)
    assert_that(response_email.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))
