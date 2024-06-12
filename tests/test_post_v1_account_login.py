import time
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_post_v1_account_login():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "User021"
    password = "resu4321"
    email = "Postman_user021@gmail.com"

    json = {
        "login": login,
        "email": email,
        "password": password
    }
    api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)

    json = {
        "login": login,
        "password": password,
        "rememberMe": False
    }
    response_login = api.login.post_v1_account_login(json=json)
    assert response_login.status_code == 200, f"Метод входа в логин завершился со статус кодом {response_login.status_code}"
