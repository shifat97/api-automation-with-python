import requests


def test_create_student(base_url, auth_header, test_create_student_data):
    # Validating create student without authorization header
    response_without_auth_header = requests.post(f"{base_url}/api/student", json=test_create_student_data)

    # Validating status code for without auth header
    assert response_without_auth_header.status_code == 401, f"Expected 401, got {response_without_auth_header.status_code}"
    # Validating message for without auth header
    assert response_without_auth_header.json().get(
        'message') == 'Missing or invalid Authorization header', f"Message should be {'Missing or invalid Authorization header'} but got {response_without_auth_header.json()['message']}"

