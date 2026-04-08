import pytest
import requests

def test_login(base_url, test_login_data):
    response = requests.post(f"{base_url}/login", json=test_login_data)
    
    # Validating status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Validating response structure
    assert "authToken" in response.json(), "Login response does not contain 'authToken'"

    # Validating if authToken is empty or not
    assert response.json(), f"authToken is empty or None"

# Testing get all students   
def test_get_students(base_url, auth_header, test_payload_structure):
    # GET ALL STUDENTS
    get_students = requests.get(f"{base_url}/api/student", headers=auth_header)
    
    # Validating status code
    assert get_students.status_code == 200, f"Expected 200, got {get_students.status_code}"

    # Extract all student info
    students = get_students.json()

    # Validating structure like key and type
    for student in students:
        for key, expected_type in test_payload_structure.items():
            # Extract type from key
            key_type = type(student.get(key))
            assert key_type == expected_type, f"Expected {expected_type}, got {key_type}"
            assert student[key] is not None, f"{key} should not be None"
    
    # students[0]["_id"] = "qq"
    # students[1]["_id"] = "qq"

    # Validating unique _id
    ids = [student["_id"] for student in students]
    assert len(ids) == len(set(ids)), 'Duplicate student IDs found'