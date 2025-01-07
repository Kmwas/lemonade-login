import requests
import json

def test_login_api(url, username, password):
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        response_json = response.json()

        if "token" in response_json:
            print("Login successful. Token:", response_json["token"])
            return True
        else:
            print("Login failed. Unexpected response:", response_json)
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return False

# Test cases
api_url = "https://test_api_endpoint" # Replace with test endpoint
test_login_api(api_url, "valid_user", "valid_password")
test_login_api(api_url, "invalid_user", "invalid_password")