from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    token = '118401c5-3cce-4b36-94b4-5aa3e21651f6'

    response = api.account.put_v1_account_token(
        token=token
    )

    print(response)
