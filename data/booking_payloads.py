VALID_BOOKING_PAYLOAD = {
    "firstname": "Aaren",
    "lastname": "QA",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-06-10",
        "checkout": "2026-06-15"
    },
    "additionalneeds": "Breakfast"
}

MISSING_FIRSTNAME_BOOKING_PAYLOAD = {
    "lastname": "QA",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-06-10",
        "checkout": "2026-06-15"
    },
    "additionalneeds": "Breakfast"
}