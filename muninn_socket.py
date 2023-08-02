import argparse
import requests
import threading

def main(method, url, data, port=80, num_requests=10, headers=None):
    """
    Sends custom repeat HTTP requests to a specified URL.

    Args:
        method (str): The request method (GET, POST, PUT, or DELETE).
        url (str): The URL of the request.
        data (str): Data to be sent in the request body in JSON format.
        port (int, optional): The connection port (default is 80).
        num_requests (int, optional): The number of repeated requests (default is 10).
        headers (dict, optional): Headers to be sent with the request.
    """
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request, args=(method, url, data, port, headers))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def send_request(method, url, data, port, headers):
    headers = headers or {}
    try:
        response = requests.request(method, url, data=data, headers=headers, timeout=10, verify=False)
        print("URL:", url)
        print("Status Code:", response.status_code)
        print("Response:")
        print(response.text)
        print("-" * 30)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
