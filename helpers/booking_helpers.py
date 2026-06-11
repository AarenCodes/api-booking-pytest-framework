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

def delete_booking(booking_id, token):
    response = requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        cookies={"token": token}
    )

    return response

def update_booking(booking_id, token, payload):
    response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=payload,
        cookies={"token": token}
    )

    return response