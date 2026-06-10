import requests

from config.settings import BASE_URL
from data.auth_payloads import INVALID_USERNAME_PAYLOAD


def test_invalid_username():
    """
    Verify authentication fails when an invalid username is provided.
    """

    print("\n[TEST] Starting invalid username authentication test")

    print(f"[REQUEST] POST {BASE_URL}/auth")

    print(
        f"[PAYLOAD] username={INVALID_USERNAME_PAYLOAD['username']} "
        f"password=********"
    )

    response = requests.post(
        f"{BASE_URL}/auth",
        json=INVALID_USERNAME_PAYLOAD
    )

    print(f"[RESPONSE] Status Code: {response.status_code}")

    response_body = response.json()

    print(f"[RESPONSE BODY] {response_body}")

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    assert "reason" in response_body, (
        f"Expected reason in response body, got {response_body}"
    )

    assert response_body["reason"] == "Bad credentials", (
        f"Expected 'Bad credentials', got {response_body}"
    )

    assert "token" not in response_body, (
        f"Expected no token to be returned, got {response_body}"
    )

    print("[PASS] Invalid username was rejected successfully")