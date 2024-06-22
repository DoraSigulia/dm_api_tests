import time
from services import *
from dm_api_account.models import *

def test_post_v1_account_login():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "Cat2"
    password = "meowmeow"
    email = "Kitty_cat2@gmail.com"

    json_account = Registration(
        login=login,
        email=email,
        password=password
    )
    api.account.post_v1_account(json=json_account)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)

    json_login = LoginCredential(
        login=login,
        password=password,
        rememberMe=False
    )
    api.login.post_v1_account_login(json=json_login)

