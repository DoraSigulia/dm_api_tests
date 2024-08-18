
def test_get_v1_account(
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
    dm_api_facade.account.activate_registered_user(login=login)
    dataset2 = orm.get_user_by_user(login=login)
    for row in dataset2:
        assert row.Activated is True, f"User {login} is not activated"
    headers = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.set_headers(headers=headers)
    dm_api_facade.account_api.get_v1_account()
