from data.booking_payloads import VALID_BOOKING_PAYLOAD, UPDATED_BOOKING_PAYLOAD
from helpers.auth_helpers import create_auth_token
from helpers.booking_helpers import create_booking, update_booking


def test_update_created_booking():
    """
    Verify a created booking can be fully updated with a valid auth token.
    """

    print("\n[TEST] Starting update booking test")

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

    print(f"[REQUEST] PUT /booking/{booking_id}")
    print(f"[PAYLOAD] {UPDATED_BOOKING_PAYLOAD}")

    update_response = update_booking(
        booking_id,
        token,
        UPDATED_BOOKING_PAYLOAD
    )

    print(f"[RESPONSE] Status Code: {update_response.status_code}")

    update_response_body = update_response.json()

    print(f"[RESPONSE BODY] {update_response_body}")

    assert update_response.status_code == 200, (
        f"Expected status code 200, got {update_response.status_code}"
    )

    assert update_response_body["firstname"] == UPDATED_BOOKING_PAYLOAD["firstname"], (
        f"Expected firstname {UPDATED_BOOKING_PAYLOAD['firstname']}, "
        f"got {update_response_body['firstname']}"
    )

    assert update_response_body["lastname"] == UPDATED_BOOKING_PAYLOAD["lastname"], (
        f"Expected lastname {UPDATED_BOOKING_PAYLOAD['lastname']}, "
        f"got {update_response_body['lastname']}"
    )

    assert update_response_body["totalprice"] == UPDATED_BOOKING_PAYLOAD["totalprice"], (
        f"Expected totalprice {UPDATED_BOOKING_PAYLOAD['totalprice']}, "
        f"got {update_response_body['totalprice']}"
    )

    assert update_response_body["depositpaid"] == UPDATED_BOOKING_PAYLOAD["depositpaid"], (
        f"Expected depositpaid {UPDATED_BOOKING_PAYLOAD['depositpaid']}, "
        f"got {update_response_body['depositpaid']}"
    )

    assert (
        update_response_body["bookingdates"]["checkin"]
        == UPDATED_BOOKING_PAYLOAD["bookingdates"]["checkin"]
    ), (
        f"Expected checkin {UPDATED_BOOKING_PAYLOAD['bookingdates']['checkin']}, "
        f"got {update_response_body['bookingdates']['checkin']}"
    )

    assert (
        update_response_body["bookingdates"]["checkout"]
        == UPDATED_BOOKING_PAYLOAD["bookingdates"]["checkout"]
    ), (
        f"Expected checkout {UPDATED_BOOKING_PAYLOAD['bookingdates']['checkout']}, "
        f"got {update_response_body['bookingdates']['checkout']}"
    )

    assert update_response_body["additionalneeds"] == UPDATED_BOOKING_PAYLOAD["additionalneeds"], (
        f"Expected additionalneeds {UPDATED_BOOKING_PAYLOAD['additionalneeds']}, "
        f"got {update_response_body['additionalneeds']}"
    )

    print("[PASS] Booking was updated successfully")