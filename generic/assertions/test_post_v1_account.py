import allure
from generic.helpers.orm_models import User
from hamcrest import assert_that, has_properties, has_entries
from dm_api_account.models.user_envelope import Roles


class AssertionsPostV1Account:

    def __init__(self, orm):
        self.orm = orm

    @allure.step("Проверка, что пользователь {login} был создан")
    def check_user_was_created(self, login):
        dataset = self.orm.get_user_by_user(login=login)
        row: User
        for row in dataset:
            assert_that(row, has_entries(
                {
                    'Login': login,
                    'Activated': False
                }
            ))

    @allure.step("Проверка по БД что пользователь активирован")
    def check_user_was_activated(self, login):
        dataset2 = self.orm.get_user_by_user(login=login)
        for row in dataset2:
            assert_that(row, has_entries(
                {
                    'Activated': True
                }
            ))

    @allure.step("Проверка, что пользователь создан с ролью GUEST и PLAYER")
    def check_user_login_and_roles(self, response_token, login):
        assert_that(response_token.resource, has_properties(
            {
                "login": login,
                "roles": [Roles.GUEST, Roles.PLAYER],
                "medium_picture_url": None
            }
        ))

    @allure.step("Проверка, что метод отдает правильное сообщение об ошибке")
    def check_error_message(self, response, check):
        assert_that(response.json(), has_entries(
            {
                'errors': check
            }
        ))
