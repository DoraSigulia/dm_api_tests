import time
from services import *
from dm_api_account.models import *


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = Registration(
        login="Cat002",
        email="Kitty_cat002@gmail.com",
        password="meowmeow"
    )
    api.account.post_v1_account(json=json, status_code=201)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)
