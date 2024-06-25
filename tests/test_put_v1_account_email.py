from services import *
from hamcrest import assert_that, has_properties


def test_put_v1_account_email():
    api = Facade(host='http://5.63.153.31:5051')
    login = "Fox12"
    email = "Fox12@gmail.com"
    new_email = "Fox13@gmail.com"
    password = "gavgav"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    response_email = api.account.change_registered_email(login=login, password=password, email=new_email)
    assert_that(response_email.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))
