import allure
import pytest
from string import ascii_letters, digits
import random


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@allure.suite("Регистрация нового пользователя с помощью метода /v1/account")
@allure.sub_suite("Позитивные проверки")
class TestPostV1Account:

    @allure.title("Регистрация нового пользователя")
    def test_post_v1_account(
            self,
            mailhog,
            dm_api_facade,
            orm,
            prepare_user,
            assertions
    ):
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password
        status_code = prepare_user.status_code
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        assertions.check_user_was_created(login=login)
        response_token = dm_api_facade.account.activate_registered_user(login=login)
        assertions.check_user_was_activated(login=login)
        assertions.check_user_login_and_roles(response_token=response_token, login=login)




    @pytest.mark.parametrize('login, email, password, status_code, check', [
        ('User', 'user@mail.ru', 'user123', 201, ''),
        ('User', 'user@mail.ru', random_string(1, 1), 400, {'Password': ['Short']}),
        ('User', 'user@mail.ru', random_string(1000, 1000), 201, ''),
        (random_string(1, 1), random_string(5, 6) + '@mail.ru', random_string(6, 10), 400, {'Login': ['Short']}),
        ('', random_string(5, 6) + '@mail.ru', random_string(6, 10), 400, {'Login': ['Empty', 'Short']}),
        (random_string(1000, 1000), random_string(5, 6) + '@mail.ru', random_string(6, 10), 400, {'Login': ['Long']}),
        ('User', '@mail.ru', random_string(6, 10), 400, {'Email': ['Invalid']}),
        ('User', random_string(6, 10), random_string(6, 10), 400, {'Email': ['Invalid']}),
    ])
    @allure.title("Регистрация нового пользователя. Проверка на сообщение {check}")
    def test_post_v1_account_with_diff_params(
            self,
            mailhog,
            dm_api_facade,
            orm,
            login,
            email,
            password,
            status_code,
            check,
            assertions
    ):
        login = login
        email = email
        password = password
        status_code = status_code
        orm.delete_user_by_login(login=login)
        dm_api_facade.mailhog.delete_message_by_login(login=login)
        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        if status_code == 201:
            assertions.check_user_was_created(login=login)
            response_token = dm_api_facade.account.activate_registered_user(login=login)
            assertions.check_user_was_activated(login=login)
            assertions.check_user_login_and_roles(response_token=response_token, login=login)

        else:
            assertions.check_error_message(response=response, check=check)
