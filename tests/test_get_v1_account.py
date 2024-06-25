from services import *


def test_get_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "Fox1"
    email = "Fox1@gmail.com"
    password = "gavgav"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    headers = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=headers)
    api.account_api.get_v1_account()
