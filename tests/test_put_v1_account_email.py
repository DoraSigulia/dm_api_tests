from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = {
        "login": "User777",
        "password": "resu4321",
        "email": "Postman_user778@gmail.com"
    }

    response = api.account.put_v1_account_email(
        json=json
    )

    print(response)
