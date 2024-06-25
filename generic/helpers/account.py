from dm_api_account.models import *


class Account:

    def __init__(self, facade):
        self.facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(
            self,
            login: str,
            email: str,
            password: str
    ):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            ))
        return response

    def get_current_user(self, **kwargs):
        return self.facade.account_api.get_v1_account(**kwargs)

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(token=token)
        return response

    def reset_registered_password(
            self,
            login: str,
            email: str,
    ):
        response = self.facade.account_api.post_v1_account_password(
            ResetPassword(
                login=login,
                email=email
            )
        )
        return response

    def change_registered_password(
            self,
            login: str,
            old_password: str,
            new_password: str
    ):
        token = self.facade.mailhog.get_reset_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_password(
            ChangePassword(
                login=login,
                token=token,
                oldPassword=old_password,
                newPassword=new_password
            )
        )
        return response

    def change_registered_email(
            self,
            login: str,
            email: str,
            password: str
    ):
        response = self.facade.account_api.put_v1_account_email(
            ChangeEmail(
                login=login,
                password=password,
                email=email
            )
        )
        return response
