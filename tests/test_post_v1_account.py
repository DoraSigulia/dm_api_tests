import time
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "User012",
        "email": "Postman_user012@gmail.com",
        "password": "resu4321"
    }
    response_account = api.account.post_v1_account(json=json)
    assert response_account.status_code == 201, f"Метод создания нового пользователя завершился со статус кодом {response_account.status_code}"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)
