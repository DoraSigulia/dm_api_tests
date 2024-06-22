from requests import Response
from dm_api_account.models import *
from dm_api_account.models import UserDetailsEnvelope, UserEnvelope
from restclient.restclient import Restclient
from dm_api_account.utilities import validate_request_json, validate_status_code


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account(
            self,
            json: Registration,
            status_code: int = 201,
            **kwargs
    ) -> Response:
        """
        Register new user
        :param json registration_model
        :return:
        """

        response = self.client.post(
            path="/v1/account",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(
            response,
            status_code
        )
        return response

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> UserDetailsEnvelope | Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path="/v1/account",
            **kwargs
        )
        validate_status_code(
            response,
            status_code
        )
        if status_code == 200:
            return UserDetailsEnvelope(**response.json())
        return response

    def put_v1_account_token(
            self,
            token,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Activate registered user
        :return:
        """
        token = token

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        validate_status_code(
            response,
            status_code
        )
        if status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Reset registered user password
        :param json reset_password_model
        :return:
        """
        response = self.client.post(
            path="/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(
            response,
            status_code
        )
        if status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Change registered user password
        :param json change_password_model
        :return:
        """
        response = self.client.put(
            path="/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(
            response,
            status_code
        )
        if status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Change registered user email
        :param json change_email_model
        :return:
        """
        response = self.client.put(
            path="/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(
            response,
            status_code
        )
        if status_code == 200:
            return UserEnvelope(**response.json())
        return response
