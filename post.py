import time
import hmac
import hashlib
import base64
import struct
import requests as r
import json

def generate_totp(email, time_step=30, digits=10):
    # Shared secret: email + "HENNGECHALLENGE004"
    secret = (email + "HENNGECHALLENGE004").encode()

    # Time counter: (current time // 30)
    T = int(time.time()) // time_step
    counter = struct.pack(">Q", T)  # 8-byte big-endian integer

    # HMAC-SHA-512
    hmac_hash = hmac.new(secret, counter, hashlib.sha512).digest()

    # Dynamic truncation
    offset = hmac_hash[-1] & 0x0F
    truncated = hmac_hash[offset:offset + 4]
    code = struct.unpack(">I", truncated)[0] & 0x7FFFFFFF  # 31-bit

    # Return TOTP code with leading zeros
    return str(code % (10 ** digits)).zfill(digits)

# Example usage:
email = "minithbmatthew@gmail.com"
totp_code = generate_totp(email)
auth_str = f"{email}:{totp_code}"
auth_header = base64.b64encode(auth_str.encode()).decode()

url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth_header}"
}

data = {
  "github_url": "https://gist.github.com/xevansz/ae7b4f0df7e79026e3af2f1449ce41e6",
  "contact_email": "minithbmatthew@gmail.com",
  "solution_language": "python"
}

response = r.post(url, headers=headers, data=json.dumps(data))

print("Status Code:", response.status_code)
print("Response:", response.text)


# Response
# Status Code: 200
# Response: {"message":"Congratulations! You have achieved mission 3"}