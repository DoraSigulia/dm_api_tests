import requests


def put_v1_account_password():
    """
    Change registered user password
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = {
        "login": "User",
        "token": "",
        "oldPassword": "resu4321",
        "newPassword": "user1234"
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )

    return response

response = put_v1_account_password()

print(response.status_code)
print(response.text)
