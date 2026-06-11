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

UPDATED_BOOKING_PAYLOAD = {
    "firstname": "Aaren",
    "lastname": "Updated",
    "totalprice": 250,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2026-07-01",
        "checkout": "2026-07-05"
    },
    "additionalneeds": "Dinner"
}