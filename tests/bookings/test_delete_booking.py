from data.booking_payloads import VALID_BOOKING_PAYLOAD
from helpers.auth_helpers import create_auth_token
from helpers.booking_helpers import create_booking, delete_booking, get_booking


def test_delete_created_booking():
    """
    Verify a created booking can be deleted by using a valid auth token.
    """

    print("\n[TEST] Starting delete booking test")

    print("[REQUEST] POST /auth")

    token = create_auth_token()

    print("[INFO] Auth token was created successfully")

    print("[REQUEST] POST /booking")
    print(f"[PAYLOAD] {VALID_BOOKING_PAYLOAD}")

    create_response = create_booking(VALID_BOOKING_PAYLOAD)

    print(f"[RESPONSE] Status Code: {create_response.status_code}")

    create_response_body = create_response.json()

    print(f"[RESPONSE BODY] {create_response_body}")

    assert create_response.status_code == 200, (
        f"Expected status code 200, got {create_response.status_code}"
    )

    assert "bookingid" in create_response_body, (
        f"Expected bookingid in response body, got {create_response_body}"
    )

    booking_id = create_response_body["bookingid"]

    print(f"[INFO] Created booking id: {booking_id}")

    print(f"[REQUEST] DELETE /booking/{booking_id}")

    delete_response = delete_booking(booking_id, token)

    print(f"[RESPONSE] Status Code: {delete_response.status_code}")
    print(f"[RESPONSE BODY] {delete_response.text}")

    assert delete_response.status_code == 201, (
        f"Expected status code 201, got {delete_response.status_code}"
    )

    print(f"[REQUEST] GET /booking/{booking_id}")

    get_response = get_booking(booking_id)

    print(f"[RESPONSE] Status Code: {get_response.status_code}")
    print(f"[RESPONSE BODY] {get_response.text}")

    assert get_response.status_code == 404, (
        f"Expected status code 404 after deleting booking, got {get_response.status_code}"
    )

    assert get_response.text == "Not Found", (
        f"Expected 'Not Found' after deleting booking, got {get_response.text}"
    )

    print("[PASS] Booking was deleted successfully")