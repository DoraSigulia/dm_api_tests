from dm_api_account.apis import *


class DmApiAccount:
    def __init__(self, host, headers=None):
        self.account = AccountApi(host, headers)
        self.login = LoginApi(host, headers)
