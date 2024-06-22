from services import *


def test_get_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    api.account.get_v1_account()
