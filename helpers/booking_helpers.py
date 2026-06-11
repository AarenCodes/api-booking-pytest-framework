import requests

from config.settings import BASE_URL


def create_booking(payload):
    response = requests.post(
        f"{BASE_URL}/booking",
        json=payload
    )

    return response

def get_booking(booking_id):
    response = requests.get(
        f"{BASE_URL}/booking/{booking_id}"
    )

    return response