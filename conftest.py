import pytest
from generic.helpers.orm_db import OrmDatabase
from services import *
from generic.helpers.mailhog import MailhogApi
from collections import namedtuple



@pytest.fixture
def mailhog():
    return MailhogApi(host='http://5.63.153.31:5025')


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(host='http://5.63.153.31:5051', mailhog=mailhog)


@pytest.fixture
def orm():
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    yield orm
    orm.db.close_connection()


@pytest.fixture
def prepare_user(
        dm_api_facade,
        orm,
        login, email, password
):
    user = namedtuple('User', 'login, email, password')
    User = user(
        login=login,
        email=email,
        password=password
    )
    orm.delete_user_by_login(login=User.login)
    dm_api_facade.mailhog.delete_message_by_login(login=User.login)
    dataset = orm.get_user_by_user(login=User.login)
    assert len(dataset) == 0
    return User
