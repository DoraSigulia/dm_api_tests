from dm_api_account.models.user_envelope import Roles
from hamcrest import assert_that, has_properties


def test_put_v1_account_token(
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
    response_token = dm_api_facade.account.activate_registered_user(login=login)
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
