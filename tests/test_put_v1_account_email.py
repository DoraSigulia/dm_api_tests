from generic.helpers.orm_models import User
from hamcrest import assert_that, has_properties


def test_put_v1_account_email(
        mailhog,
        dm_api_facade,
        orm,
        prepare_user
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
    new_email = "Fox@gmail.com"
    dm_api_facade.account.activate_registered_user(login=login)
    response_email = dm_api_facade.account.change_registered_email(login=login, password=password, email=new_email)
    dataset = orm.get_user_by_user(login=login)
    row: User
    for row in dataset:
        assert row.Email == new_email, f"New email is not {new_email}, actual email is {row.Email}"

    assert_that(response_email.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))

