from generic.helpers.orm_db import OrmDatabase
from services import *
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope import Roles


def test_put_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    login = "Cat"
    email = "Cat@gmail.com"
    old_password = "meowmeow"
    new_password = "gavgav"
    orm.delete_user_by_login(login=login)
    api.mailhog.delete_message_by_login(login=login)

    api.account.register_new_user(
        login=login,
        email=email,
        password=old_password
    )
    api.account.activate_registered_user(login=login)
    api.account.reset_registered_password(
        login=login,
        email=email
    )
    headers = api.login.get_auth_token(login=login, password=old_password)
    api.account.set_headers(headers=headers)

    response_password = api.account.change_registered_password(
        login=login,
        old_password=old_password,
        new_password=new_password)

    assert_that(response_password.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))
    assert_that(response_password.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))
    orm.db.close_connection()
