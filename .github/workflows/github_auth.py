import jwt
import time

APP_ID: ${{secrets.YOUR_APP_ID}}
private_key = os.getenv("YOUR_PEM_FILE")

payload = {
   "iat": int(time.time()),
    "exp": int(time.time()) + 600,
    "iss": APP_ID, 
}

encoded_jwt = jwt.encode(payload,private_key,algorithm="RS256")
print(encoded_jwt)
