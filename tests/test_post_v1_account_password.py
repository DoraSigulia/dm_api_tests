from services.dm_api_account import DmApiAccount


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "User777",
        "email": "Postman_user777@gmail.com"
    }

    response = api.account.post_v1_account_password(
        json=json
    )

    print(response)
