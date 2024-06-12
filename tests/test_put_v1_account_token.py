import time
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_token():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "User015",
        "email": "Postman_user015@gmail.com",
        "password": "resu4321"
    }
    api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response_token = api.account.put_v1_account_token(token=token)
    assert response_token.status_code == 200, f"Метод активации нового пользователя завершился со статус кодом {response_token.status_code}"
