import time
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.orm_models import User
from services import *
from dm_api_account.models.user_envelope import Roles
from hamcrest import assert_that, has_properties


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    login = "Cat"
    email = "Cat@gmail.com"
    password = "meowmeow"
    orm.delete_user_by_login(login=login)
    api.mailhog.delete_message_by_login(login=login)
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = orm.get_user_by_user(login=login)
    row: User
    for row in dataset:
        assert row.Login == login, f"User {login} is not found"
        assert row.Activated is False, f"User {login} is not activated"

    response_token = api.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset2 = orm.get_user_by_user(login=login)
    for row in dataset2:
        assert row.Activated is True, f"User {login} is not activated"

    assert_that(response_token.resource, has_properties(
        {
            "login": login,
            "roles": [Roles.GUEST, Roles.PLAYER],
            "medium_picture_url": None
        }
    ))
    orm.db.close_connection()
