import json
import time
from requests import Response
from restclient.restclient import Restclient


def decorator(fn):
    def wrapper(*args, **kwargs):
        for i in range(5):
            response = fn(*args, **kwargs)
            emails = response.json()['items']
            if len(emails) < 5:
                print(f'--- attempt {i} ---')
                time.sleep(1)
                continue
            else:
                return response

    return wrapper


class MailhogApi:
    def __init__(self, host='http://5.63.153.31:5025'):
        self.host = host
        self.client = Restclient(host=host)

    @decorator
    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        response = self.client.get(
            path='/api/v2/messages',
            params={
                'limit': limit
            })
        return response

    def delete_api_v1_messages(self, id_message: str):
        """
        Delete message by login
        :id_massage:
        """
        self.client.delete(
            path=f'/api/v1/messages/{id_message}'
        )

    def get_api_v2_search(self, query) -> Response:
        """
        Get messages by query
        :param query:
        :return:
        """
        response = self.client.get(
            path='',
            params={
                'query': query,
                'kind': 'containing'
            }
        )
        return response

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from last email
        :return:
        """
        email = self.get_api_v2_messages(limit=1).json()
        token_url = (json.loads(email['items'][0]['Content']['Body']))['ConfirmationLinkUrl']
        return token_url.split('/')[-1]

    def get_token_from_last_email_by_name(self, login) -> str:
        """
        Get user activation token from last email after search by name
        :return:
        """
        self.get_api_v2_search(query=login)
        email = self.get_api_v2_messages(limit=1).json()
        token_url = (json.loads(email['items'][0]['Content']['Body']))['ConfirmationLinkUri']
        return token_url.split('/')[-1]

    def get_token_by_login(
            self,
            login: str,
            limit: int = 5,
            attempt: int = 5
    ):
        if attempt == 0:
            raise AssertionError(f"Пользователь с логином {login} не найден")
        emails = self.get_api_v2_messages(limit=limit).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                print(token)
                return token
        time.sleep(1)
        return self.get_token_by_login(login=login, attempt=attempt - 1)

    def get_reset_token_by_login(
            self,
            login: str,
            limit: int = 5,
            attempt: int = 5
    ):
        if attempt == 0:
            raise AssertionError(f"Пользователь с логином {login} не найден")
        emails = self.get_api_v2_messages(limit=limit).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                token = user_data['ConfirmationLinkUri'].split('/')[-1]
                print(token)
                return token
        time.sleep(1)
        return self.get_token_by_login(login=login, attempt=attempt - 1)

    def delete_message_by_login(
            self,
            login: str,
            limit: int = 5,
            attempt: int = 5
    ):
        if attempt == 0:
            raise AssertionError(f"Пользователь с логином {login} не найден")
        emails = self.get_api_v2_messages(limit=limit).json()['items']
        for email in emails:
            if login == json.loads(email['Content']['Body']).get('Login'):
                id_message = email['ID']
                self.delete_api_v1_messages(id_message)
                return
        time.sleep(1)
        return self.delete_message_by_login(login=login, attempt=attempt - 1)
