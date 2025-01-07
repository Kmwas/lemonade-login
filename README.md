# Lemonade Login API Test Script

This Python script tests a login API using POST requests. It sends requests with both valid and invalid credentials and checks the API's response.

## Prerequisites

*   Python 3.x
*   `requests` library: You can install it using pip:

    ```bash
    pip install requests
    ```

## How to Use

1.  **Clone the repository (if you haven't already):**

    ```bash
    git clone [https://github.com/Kmwas/lemonade-login.git](https://github.com/Kmwas/lemonade-login.git) # Replace with your repo URL
    cd lemonade-login
    ```

2.  **Replace the test API endpoint:**

    Open `test_login_api.py` and replace `"https://test_api_endpoint"` with the actual URL of the API you want to test. *Do not use a production API endpoint for testing.*

    ```python
    api_url = "https://your_test_api_endpoint" # Replace with your test endpoint
    ```

3.  **Run the script:**

    ```bash
    python test_login_api.py
    ```

## Code Explanation

The script uses the `requests` library to send POST requests to the login API. The `test_login_api` function takes a username and password as arguments, sends the request, and checks the response for a "token" upon successful authentication. It also handles potential errors during the request.
