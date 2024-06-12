from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    token = '118401c5-3cce-4b36-94b4-5aa3e21651f6'
    json = {
        "login": "User777",
        "email": "Postman_user777@gmail.com",
        "password": "resu4321"
    }

    response_account = api.account.post_v1_account(
        json=json
    )
    response_token = api.account.put_v1_account_token(
        token=token
    )
    print(response_account)
    print(response_token)
