from services import *
from generic.helpers.orm_db import OrmDatabase


def test_post_v1_account_login():
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
    api.login.authenticate_via_credentials(login=login, password=password)
    orm.db.close_connection()
