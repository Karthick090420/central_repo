import requests
import sys

REPO_OWNER = "karthick090420"
REPO_NAME = "cnetral_repo"
WORKFLOW_FILE = "sample.yml"

GITHUB_TOKEN = "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"

repository_url = sys.argv[1]

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"

payload = {
"ref": "main",
"inputs": {
"repository_url": repository_url
}
}

headers = {
"Authorization": f"Bearer {GITHUB_TOKEN}",
"Accept": "application/vnd.github+json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)
