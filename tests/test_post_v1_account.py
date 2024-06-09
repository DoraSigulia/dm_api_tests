from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "User777",
        "email": "Postman_user777@gmail.com",
        "password": "resu4321"
    }

    response = api.account.post_v1_account(
        json=json
    )
    print(response)
