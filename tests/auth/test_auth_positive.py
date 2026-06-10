import requests

from config.settings import BASE_URL
from data.auth_payloads import VALID_AUTH_PAYLOAD


def test_create_auth_token():
    """
    Verify valid credentials generate an authentication token.
    """

    print("\n[TEST] Starting authentication token test")

    print(f"[REQUEST] POST {BASE_URL}/auth")

    print(
        f"[PAYLOAD] username={VALID_AUTH_PAYLOAD['username']} "
        f"password=********"
    )

    response = requests.post(
        f"{BASE_URL}/auth",
        json=VALID_AUTH_PAYLOAD
    )

    print(f"[RESPONSE] Status Code: {response.status_code}")

    response_body = response.json()

    print(f"[RESPONSE BODY] {response_body}")

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    assert "token" in response_body, (
        f"Expected token in response body, got {response_body}"
    )

    token = response_body["token"]

    print(f"[TOKEN] Generated token: {token[:8]}...")

    assert token, (
        "Expected token value to not be empty"
    )

    print("[PASS] Authentication token generated successfully")