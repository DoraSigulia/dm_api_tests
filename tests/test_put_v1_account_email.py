import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "User016"
    password = "resu4321"
    old_email = "Postman_user016@gmail.com"
    new_email = "Postman_user017@gmail.com"

    json_account = {
        "login": login,
        "email": old_email,
        "password": password
    }
    api.account.post_v1_account(json=json_account)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)

    json_email = {
        "login": login,
        "password": password,
        "email": new_email
    }
    response_email = api.account.put_v1_account_email(json=json_email)
    assert response_email.status_code == 200, f"Метод смены email завершился со статус кодом {response_email.status_code}"
