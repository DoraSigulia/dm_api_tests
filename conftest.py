import pytest

from generic.assertions.test_post_v1_account import AssertionsPostV1Account
from generic.helpers.orm_db import OrmDatabase
from services import *
from generic.helpers.mailhog import MailhogApi
from collections import namedtuple
from vyper import v
from pathlib import Path


@pytest.fixture
def mailhog():
    host = v.get('services.mailhog')
    return MailhogApi(host=host)


@pytest.fixture
def dm_api_facade(mailhog, request):
    host = v.get('services.dm_api_account')
    return Facade(host=host, mailhog=mailhog)


@pytest.fixture
def orm():
    orm = OrmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database'))
    yield orm
    orm.db.close_connection()


@pytest.fixture()
def assertions(orm):
    return AssertionsPostV1Account(orm)


options = (
    'services.dm_api_account',
    'services.mailhog',
    'database.dm3_5.host'
)


@pytest.fixture
def prepare_user(
        dm_api_facade,
        orm
):
    user = namedtuple('User', 'login, email, password, status_code')
    User = user(
        login='User',
        email='user@mail.ru',
        password='user123',
        status_code=201
    )
    orm.delete_user_by_login(login=User.login)
    dm_api_facade.mailhog.delete_message_by_login(login=User.login)
    dataset = orm.get_user_by_user(login=User.login)
    assert len(dataset) == 0
    return User


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
