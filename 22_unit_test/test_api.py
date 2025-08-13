# test_api.py
import requests

BASE_URL = 'http://127.0.0.1:5000'


def test_register_success():
    """Testing is registration endpoint working"""
    payload = {
        'username': 'new-user',
        'password': 'secure-password'
    }
    response = requests.post(f'{BASE_URL}/register', json=payload)
    # assert 201 is the HTTP status code for "Created"
    assert response.status_code == 201
    assert 'User registered successfully' in response.json()['message']


def test_register_missing_fields():
    """Testing if registration failed and data is incomplete"""
    payload = {
        'username': 'incomplete_user'
    }
    response = requests.post(f'{BASE_URL}/register', json=payload)
    # assert 400 is the HTTP status code for "Bad Request"
    assert response.status_code == 400
    assert 'Username and password are required' in response.json()['message']


def test_login_success():
    """Test to ensure login is successful with correct credentials."""
    payload = {
        'username': 'testuser',
        'password': 'testpass'
    }
    response = requests.post(f'{BASE_URL}/login', json=payload)
    # assert 200 is the HTTP status code for "OK"
    assert response.status_code == 200
    assert 'Login successful' in response.json()['message']


def test_login_fail():
    """Test to ensure login fails with incorrect credentials."""
    payload = {
        'username': 'wrong_user',
        'password': 'wrong_password'
    }
    response = requests.post(f'{BASE_URL}/login', json=payload)
    # assert 401 is the HTTP status code for "Unauthorized"
    assert response.status_code == 401
    assert 'Invalid credentials' in response.json()['message']
