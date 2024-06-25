from dm_api_account.apis import *
from generic.helpers import *
from generic.helpers.mailhog import MailhogApi


class Facade:
    def __init__(self, host, mailhog_host=None, headers=None):
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = MailhogApi()
        self.account = Account(self)
        self.login = Login(self)
