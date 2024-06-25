from services import *


def test_delete_v1_account_login():
    api = Facade(host='http://5.63.153.31:5051')
    login = "Fox7"
    email = "Fox7@gmail.com"
    password = "gavgav"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    headers = api.login.get_auth_token(login=login, password=password)
    api.login.set_headers(headers=headers)
    api.login.logout_current_user()
