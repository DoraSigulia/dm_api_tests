import time
from dm_api_account.models.registration import Registration
from dm_api_account.models.reset_password import ResetPassword
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    login = "Cat3"
    password = "meowmeow"
    email = "Kitty_cat3@gmail.com"

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
    assert response.status_code == 200, f"Метод входа в логин завершился со статус кодом {response.status_code}"
