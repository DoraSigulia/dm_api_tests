import requests
import json

url = "http://5.63.153.31:5051/v1/account/login"

payload = json.dumps({
  "login": "User",
  "password": "resu4321",
  "rememberMe": False
})
headers = {
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

