import requests
import json

url = "http://5.63.153.31:5051/v1/account/password"

payload = json.dumps({
  "login": "User",
  "token": "",
  "oldPassword": "resu4321",
  "newPassword": "user1234"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
