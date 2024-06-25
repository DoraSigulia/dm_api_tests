from services import *


def test_post_v1_account_login():
    api = Facade(host='http://5.63.153.31:5051')
    login = "Fox9"
    email = "Fox9@gmail.com"
    password = "gavgav"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    api.login.authenticate_via_credentials(login=login, password=password)
