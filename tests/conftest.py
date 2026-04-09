import pytest
import requests
import math, random
from faker import Faker

@pytest.fixture
def base_url():
    return "http://54.255.195.111:5171"

@pytest.fixture
def auth_token(base_url, test_login_data):
    response = requests.post(f"{base_url}/login", json=test_login_data)
    token = response.json().get('authToken')

    return token

@pytest.fixture
def auth_header(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}"
    }

@pytest.fixture
def test_login_data():
    payload = {
        "username": "admin",
        "password": "password123"
    }

    return payload

@pytest.fixture
def test_payload_structure():
    structure = {
        "_id": str,
        "name": str,
        "email": str,
        "department": str,
        "registrationId": int,
        "age": int
    }

    return structure

@pytest.fixture()
def test_create_student_data():
    return {
        "name": Faker().name(),
        "email": Faker().email(),
        "department": "CSE",
        "registrationId": Faker().unique.random_number(digits=6),
        "age": Faker().random_number(digits=2)
    }