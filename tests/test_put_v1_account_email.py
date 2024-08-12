from generic.helpers.orm_db import OrmDatabase
from generic.helpers.orm_models import User
from services import *
from hamcrest import assert_that, has_properties


def test_put_v1_account_email():
    api = Facade(host='http://5.63.153.31:5051')
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    login = "Cat"
    email = "Cat@gmail.com"
    new_email = "Fox@gmail.com"
    password = "meowmeow"
    orm.delete_user_by_login(login=login)
    api.mailhog.delete_message_by_login(login=login)

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    response_email = api.account.change_registered_email(login=login, password=password, email=new_email)
    dataset = orm.get_user_by_user(login=login)
    row: User
    for row in dataset:
        assert row.Email == new_email, f"New email is not {new_email}, actual email is {row.Email}"

    assert_that(response_email.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))
    orm.db.close_connection()
