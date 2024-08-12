import structlog
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.orm_models import User

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_orm():
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    login = 'Cat'
    dataset = orm.get_user_by_user(login=login)
    row: User
    for row in dataset:
        print(row.Login)
        print(row.Name)
        print(row.Email)
        print(row.Activated)
    orm.db.close_connection()
