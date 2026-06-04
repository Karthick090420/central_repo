import time
import jwt
import requests
import sys

# -------------------------

# GitHub App Configuration

# -------------------------

APP_ID = "3688428"
INSTALLATION_ID = "131718272"

PRIVATE_KEY_FILE = "dempkarthick.2026-06-04.private-key.pem"

REPO_OWNER = "Karthick090420"
REPO_NAME = "central_repo"
WORKFLOW_FILE = "sample.yml"

# -------------------------

# Repository URL Input

# -------------------------

repository_url = sys.argv[1]

# -------------------------

# Generate GitHub App JWT

# -------------------------

with open(PRIVATE_KEY_FILE, "r") as f:
private_key = f.read()

payload = {
"iat": int(time.time()) - 60,
"exp": int(time.time()) + 600,
"iss": APP_ID
}

jwt_token = jwt.encode(
payload,
private_key,
algorithm="RS256"
)

# -------------------------

# Get Installation Token

# -------------------------

headers = {
"Authorization": f"Bearer {jwt_token}",
"Accept": "application/vnd.github+json"
}

token_url = (
f"https://api.github.com/app/installations/"
f"{INSTALLATION_ID}/access_tokens"
)

token_response = requests.post(
token_url,
headers=headers
)

if token_response.status_code != 201:
print("Failed to obtain installation token")
print(token_response.status_code)
print(token_response.text)
sys.exit(1)

installation_token = token_response.json()["token"]

print("Installation token generated successfully")

# -------------------------

# Trigger Workflow

# -------------------------

workflow_url = (
f"https://api.github.com/repos/"
f"{REPO_OWNER}/{REPO_NAME}"
f"/actions/workflows/{WORKFLOW_FILE}/dispatches"
)

workflow_headers = {
"Authorization": f"Bearer {installation_token}",
"Accept": "application/vnd.github+json"
}

payload = {
"ref": "main",
"inputs": {
"repository_url": repository_url
}
}

response = requests.post(
workflow_url,
json=payload,
headers=workflow_headers
)

print("Status:", response.status_code)
print(response.text)
