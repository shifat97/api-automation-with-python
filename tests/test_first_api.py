import requests

BASE_URL = "http://54.255.195.111:5171"

payload = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(f"{BASE_URL}/login", json=payload)

print(response.status_code)
print(response.text)