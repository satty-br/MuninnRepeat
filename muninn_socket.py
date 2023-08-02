import socket
import argparse
import ssl
import threading


def main(method, url, data, port=80, num_requests=10, headers = None):
    """
    Sends custom repeat HTTP requests to a specified URL.

    Args:
        method (str): The request method (GET, POST, PUT, or DELETE).
        url (str): The URL of the request.
        data (str): Data to be sent in the request body in JSON format.
        port (int, optional): The connection port (default is 80).
        num_requests (int, optional): The number of repeated requests (default is 10).
    """
    scheme = "http"
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
        scheme = "https"
        if port == 80:
            port = 443

    domain, *path = url.split("/", 1)
    endpoint = "/" + path[0] if path else "/"
    request_body, last_byte = parse_data(domain, endpoint, method, data,headers)
    do_request(domain, port, num_requests, scheme, request_body, last_byte)


def do_request(domain, port, num_requests, scheme, request_body, last_byte=None):
    threads = []
    clis = []
    for _ in range(num_requests):
        cli = create_socket_cli(scheme, domain, port)
        clis.append(cli)
        thread = None
        if last_byte:
            send_data(cli, request_body)
            request_body = last_byte
        thread = threading.Thread(target=send_data, args=(cli, request_body))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    for client_socket in clis:
        get_return_from_socket(client_socket)
        client_socket.close()


def get_return_from_socket(client_socket):
    response = b""
    response = client_socket.recv(4096)
   
    response_str = response.decode()

    print("socket response:")
    print(response_str)


def send_data(cli, data):
    cli.send(data.encode())


def create_socket_cli(scheme, domain, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((domain, port))
    if scheme == "https":
        context = ssl.create_default_context()
        return context.wrap_socket(client_socket, server_hostname=domain)
    return client_socket


def send_last_data(client_socket, last_char):
    client_socket.send(last_char.encode())


def parse_data(domain, endpoint, method, data,headers):
    last_character = None
    headers_str = ""
    if headers:
        headers_str = "\r\n".join([f"{key}: {value}" for key, value in headers.items()]) + "\r\n"
    request_body = f"{method.upper()} {endpoint} HTTP/1.1\r\n" \
        f"Host: {domain}\r\n" \
        f"{headers_str}" \

    if data:
        data = data.strip()
        characters_except_last = data[:-1]
        last_character = data[-1]
        request_body = f"{request_body}" \
            f"Content-Type: application/json\r\n" \
            f"Content-Length: {len(data)}\r\n\r\n" \
            f"{characters_except_last}"
    
    return request_body, last_character

