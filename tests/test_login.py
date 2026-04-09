import requests


def test_login(base_url, test_login_data):
    response = requests.post(f"{base_url}/login", json=test_login_data)

    # Validating status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Validating response structure
    assert "authToken" in response.json(), "Login response does not contain 'authToken'"

    # Validating if authToken is empty or not
    assert response.json(), f"authToken is empty or None"
