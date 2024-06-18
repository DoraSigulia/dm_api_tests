import json
from requests import Response
from restclient.restclient import Restclient


class MailhogApi:
    def __init__(self, host='http://5.63.153.31:5025'):
        self.host = host
        self.client = Restclient(host=host)

    def get_api_v2_massages(self, limit: int = 50) -> Response:
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
        email = self.get_api_v2_massages(limit=1).json()
        token_url = (json.loads(email['items'][0]['Content']['Body']))['ConfirmationLinkUrl']
        return token_url.split('/')[-1]

    def get_token_from_last_email_by_name(self, login) -> str:
        """
        Get user activation token from last email after search by name
        :return:
        """
        self.get_api_v2_search(query=login)
        email = self.get_api_v2_massages(limit=1).json()
        token_url = (json.loads(email['items'][0]['Content']['Body']))['ConfirmationLinkUri']
        return token_url.split('/')[-1]
