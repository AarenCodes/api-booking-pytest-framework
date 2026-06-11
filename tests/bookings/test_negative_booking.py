import requests

from config.settings import BASE_URL
from data.booking_payloads import MISSING_FIRSTNAME_BOOKING_PAYLOAD


def test_create_booking_missing_firstname():
    """
    Verify booking creation fails when firstname is missing.
    """

    print("\n[TEST] Starting create booking missing firstname test")

    print(f"[REQUEST] POST {BASE_URL}/booking")

    print(f"[PAYLOAD] {MISSING_FIRSTNAME_BOOKING_PAYLOAD}")

    response = requests.post(
        f"{BASE_URL}/booking",
        json=MISSING_FIRSTNAME_BOOKING_PAYLOAD
    )

    print(f"[RESPONSE] Status Code: {response.status_code}")
    print(f"[RESPONSE BODY] {response.text}")

    assert response.status_code in [400, 500], (
    f"Expected status code 400 or 500 for missing firstname, got {response.status_code}"
    )

    assert "bookingid" not in response.text, (
        f"Expected no bookingid to be returned, got {response.text}"
    )

    print("[PASS] Missing firstname booking request was rejected successfully")