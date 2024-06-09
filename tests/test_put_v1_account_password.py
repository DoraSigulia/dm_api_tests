from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = {
        "login": "User777",
        "token": "6d77190f-11a5-4898-854a-fa86490cf24f",
        "oldPassword": "resu4321",
        "newPassword": "user1234"
    }

    response = api.account.put_v1_account_password(
        json=json
    )

    print(response)
