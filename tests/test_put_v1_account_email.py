import time
from dm_api_account.models.change_email import ChangeEmail
from dm_api_account.models.registration import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "Cat4"
    password = "meowmeow"
    old_email = "Kitty_cat4@gmail.com"
    new_email = "Kitty_cat5@gmail.com"

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
    assert response_email.status_code == 200, f"Метод смены email завершился со статус кодом {response_email.status_code}"
