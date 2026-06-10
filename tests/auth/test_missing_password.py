import requests

from config.settings import BASE_URL
from data.auth_payloads import MISSING_PASSWORD_PAYLOAD


def test_missing_password():
    """
    Verify authentication fails when password is missing.
    """
    print("\n[TEST] Starting missing password sign-in test")

    print(f"[REQUEST] POST {BASE_URL}/auth")

    print(
        f"[PAYLOAD] username=admin"
        f"password=<missing>"
    )

    response = requests.post(
        f"{BASE_URL}/auth",
        json=MISSING_PASSWORD_PAYLOAD
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

    print("[PASS] Missing password was rejected successfully")