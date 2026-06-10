import requests
from config.settings import BASE_URL


def test_api_health_check():
    """
    Verify the Restful Booker API is available and responding.
    """

    response = requests.get(f"{BASE_URL}/ping")

    assert response.status_code == 201, (
        f"Expected status code 201, got {response.status_code}"
    )