import requests
import json

url = "http://5.63.153.31:5051/v1/account"

payload = json.dumps({
  "login": "User",
  "email": "Postman_user@gmail.com",
  "password": "resu4321"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)
