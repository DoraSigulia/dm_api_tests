from typing import List

import allure

from orm_client.orm_client import OrmClient
from sqlalchemy import select, delete
from generic.helpers.orm_models import User


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    @allure.step('Запрос данных из БД о всех пользователях')
    def get_all_users(self):
        query = select(User)
        dataset = self.db.send_query(query=query)
        return dataset

    @allure.step('Запрос данных из БД о пользователе с логином {login}')
    def get_user_by_user(self, login) -> List[User]:
        query = select(User).where(
            User.Login == login
        )
        dataset = self.db.send_query(query=query)
        return dataset

    @allure.step('Удаление из базы данных о пользователе с логином {login}')
    def delete_user_by_login(self, login):
        query = delete(User).where(
            User.Login == login
        )
        dataset = self.db.send_bulk_query(query=query)
        return dataset
