
import time
import jwt
import requests


print("Github Actions Runnings Successfully ")
print("Python automation started")
== == == =

APP_ID = "3688428"
INSTALLATION_ID = "131718272"

with open("demo.pem", "r") as f:
    private_key = f.read()

payload = {
    "iat": int(time.time()),
    "exp": int(time.time()) + 600,
    "iss": APP_ID,
}

jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Accept": "application/vnd.github+json",
}

url = f"https://api.github.com/app/installations/131718272/access_tokens"

response = requests.post(url, headers=headers)

access_token = response.json()["token"]

print("Installation Token Generated Successfully")

repo_headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github+json",
}

repo_url = "https://api.github.com/repos/karthick090420/AI/contents"

repo_response = requests.get(repo_url, headers=repo_headers)

print("\nRepository Files:\n")

for file in repo_response.json():
    print(file["name"])
