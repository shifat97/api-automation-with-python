import requests


def test_create_student(base_url, auth_header, test_create_student_data):
    payload = {}

    # Creating payload without email
    for k, v in test_create_student_data.items():
        if k != "email":
            payload[k] = v

    # Validating create student without authorization header
    response_without_auth_header = requests.post(f"{base_url}/api/student", json=payload)

    # Validating status code for without auth header
    assert response_without_auth_header.status_code == 401, f"Expected 401, got {response_without_auth_header.status_code}"
    # Validating message for without auth header
    assert response_without_auth_header.json().get('message') == 'Missing or invalid Authorization header', \
        f"Message should be {'Missing or invalid Authorization header'} but got {response_without_auth_header.json()['message']}"

    # Validating student creation without email field
    response_without_email = requests.post(f"{base_url}/api/student", json=payload, headers=auth_header)
    # Validating status code
    assert response_without_email.status_code == 400, f"Expected 400, got {response_without_email.status_code}"
    # Validating message
    assert response_without_email.json().get('error') == "Email is required", \
        f"Expected message to be {'Email is required'}, got {response_without_email.json().get('error')}"


    # Validating student creation with all field
    # Expected result: 200 or 201, Status: OK
    response = requests.post(f"{base_url}/api/student", json=test_create_student_data, headers=auth_header)
    # Validating status code
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    # Validating response payload
    response_payload = response.json()
    for key, expected_value in test_create_student_data.items():
        actual_value = response_payload.get(key)
        assert actual_value == expected_value, f"{key}: expected {expected_value}, got {actual_value}"
        assert actual_value is not None, f"{key} should not be None"