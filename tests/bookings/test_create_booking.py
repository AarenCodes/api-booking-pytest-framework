import requests

from config.settings import BASE_URL
from data.booking_payloads import VALID_BOOKING_PAYLOAD

def test_create_booking():
    """
    Verify that a booking can be created successfully.
    """

    print("\n[TEST] Starting create booking test")

    print(f"[REQUEST] POST {BASE_URL}/booking")

    print(f"[PAYLOAD] {VALID_BOOKING_PAYLOAD}")

    response = requests.post(
        f"{BASE_URL}/booking",
        json=VALID_BOOKING_PAYLOAD
    )

    print(f"[RESPONSE] Status Code: {response.status_code}")

    response_body = response.json()

    print(f"[RESPONSE BODY] {response_body}")

    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}"
    )

    assert "bookingid" in response_body, (
        f"Expected bookingid in response body, got {response_body}"
    )

    print("[PASS] Booking was created successfully")