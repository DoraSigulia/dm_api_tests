from requests import Response
from dm_api_account.models.login_credential import LoginCredential
from dm_api_account.models.user_envelope import UserEnvelope
from restclient.restclient import Restclient


class LoginApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account_login(self, json: LoginCredential, **kwargs) -> Response:
        """
        Authenticate via credentials
        :param json login_credential_model
        :return:
        """

        response = self.client.post(
            path="/v1/account/login",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def delete_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            path="/v1/account/login",
            **kwargs
        )
        return response

    def delete_v1_account_login_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            path="/v1/account/login/all",
            **kwargs
        )
        return response
