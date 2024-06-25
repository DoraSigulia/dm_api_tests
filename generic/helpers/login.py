from dm_api_account.models import LoginCredential


class Login:

    def __init__(self, facade):
        self.facade = facade

    def set_headers(self, headers):
        self.facade.login_api.client.session.headers.update(headers)

    def authenticate_via_credentials(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ):
        response = self.facade.login_api.post_v1_account_login(
            LoginCredential(
                login=login,
                password=password,
                rememberMe=remember_me
            )
        )
        return response

    def get_auth_token(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ):
        response = self.authenticate_via_credentials(
            login=login,
            password=password,
            remember_me=remember_me)
        token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
        return token

    def logout_current_user(self, **kwargs):
        return self.facade.login_api.delete_v1_account_login(**kwargs)

    def logout_from_every_device(self, **kwargs):
        return self.facade.login_api.delete_v1_account_login_all(**kwargs)
