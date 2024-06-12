from requests import Response
from ..models import registration_model
from ..models import reset_password_model
from ..models import change_password_model
from ..models import change_email_model
from restclient.restclient import Restclient


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        Register new user
        :param json registration_model
        :return:
        """

        response = self.client.post(
            path="/v1/account",
            json=json,
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

        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        Reset registered user password
        :param json reset_password_model
        :return:
        """
        response = self.client.post(
            path="/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_password(self, json: change_password_model, **kwargs) -> Response:
        """
        Change registered user password
        :param json change_password_model
        :return:
        """
        response = self.client.put(
            path="/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_email(self, json: change_email_model, **kwargs) -> Response:
        """
        Change registered user email
        :param json change_email_model
        :return:
        """
        response = self.client.put(
            path="/v1/account/email",
            json=json,
            **kwargs
        )

        return response
