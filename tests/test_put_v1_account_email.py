import time
from services import *
from dm_api_account.models import *


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "Cat40"
    password = "meowmeow"
    old_email = "Kitty_cat40@gmail.com"
    new_email = "Kitty_cat50@gmail.com"

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
    api.account.put_v1_account_email(json=json_email)

