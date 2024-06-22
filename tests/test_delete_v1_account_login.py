from services import *


def test_delete_v1_account_login():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    api.login.delete_v1_account_login()
