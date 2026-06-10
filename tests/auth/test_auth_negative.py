import requests

from config.settings import BASE_URL
from data.auth_payloads import (
    INVALID_USERNAME_PAYLOAD,
    INVALID_PASSWORD_PAYLOAD,
    MISSING_USERNAME_PAYLOAD,
    MISSING_PASSWORD_PAYLOAD
)


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


def test_invalid_password():
    """
    Verify authentication fails when an invalid password is provided.
    """

    print("\n[TEST] Starting invalid password authentication test")

    print(f"[REQUEST] POST {BASE_URL}/auth")

    print(
        f"[PAYLOAD] username={INVALID_PASSWORD_PAYLOAD['username']} "
        f"password=********"
    )

    response = requests.post(
        f"{BASE_URL}/auth",
        json=INVALID_PASSWORD_PAYLOAD
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

    print("[PASS] Invalid password was rejected successfully")


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


def test_missing_username():
    
    """
    Verify authentication fails when username is missing.
    """

    print("\n[TEST] Starting missing username authentication test")

    print(f"[REQUEST] POST {BASE_URL}/auth")

    print(
        "[PAYLOAD] username=<missing> "
        "password=********"
    )

    response = requests.post(
        f"{BASE_URL}/auth",
        json=MISSING_USERNAME_PAYLOAD
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

    print("[PASS] Missing username was rejected successfully")