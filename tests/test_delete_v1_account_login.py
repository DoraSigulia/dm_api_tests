from generic.helpers.orm_db import OrmDatabase
from services import *


def test_delete_v1_account_login():
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
    api.account.activate_registered_user(login=login)
    headers = api.login.get_auth_token(login=login, password=password)
    api.login.set_headers(headers=headers)
    api.login.logout_current_user()
    orm.db.close_connection()
