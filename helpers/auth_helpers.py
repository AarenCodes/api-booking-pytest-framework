import requests

from config.settings import BASE_URL
from data.auth_payloads import VALID_AUTH_PAYLOAD


def create_auth_token():
    response = requests.post(
        f"{BASE_URL}/auth",
        json=VALID_AUTH_PAYLOAD
    )

    response_body = response.json()

    return response_body["token"]