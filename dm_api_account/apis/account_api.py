from requests import Response
from dm_api_account.models.registration import Registration
from dm_api_account.models.reset_password import ResetPassword
from dm_api_account.models.change_password import ChangePassword
from dm_api_account.models.change_email import ChangeEmail
from dm_api_account.models.user_details_envelope import UserDetailsEnvelope
from dm_api_account.models.user_envelope import UserEnvelope
from restclient.restclient import Restclient


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account(self, json: Registration, **kwargs) -> Response:
        """
        Register new user
        :param json registration_model
        :return:
        """

        response = self.client.post(
            path="/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path="/v1/account",
            **kwargs
        )
        UserDetailsEnvelope(**response.json())
        return response

    def put_v1_account_token(self, token, **kwargs) -> Response:
        """
        Activate registered user
        :return:
        """
        token = token

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def post_v1_account_password(self, json: ResetPassword, **kwargs) -> Response:
        """
        Reset registered user password
        :param json reset_password_model
        :return:
        """
        response = self.client.post(
            path="/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePassword, **kwargs) -> Response:
        """
        Change registered user password
        :param json change_password_model
        :return:
        """
        response = self.client.put(
            path="/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmail, **kwargs) -> Response:
        """
        Change registered user email
        :param json change_email_model
        :return:
        """
        response = self.client.put(
            path="/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response
