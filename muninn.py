import argparse
import muninn_requests
import muninn_socket


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send custom HTTP requests.")
    parser.add_argument("--type", choices=["SOCKET", "REQUESTS"], 
                        help="use socket or requests lib?",default="HTTP")
    parser.add_argument("--method", choices=["GET", "POST", "PUT", "DELETE"],
                        help="Request method (GET, POST, PUT, or DELETE)")
    parser.add_argument("--url", required=True, help="URL of the request")
    parser.add_argument("--repeats", type=int, required=True, help="Number of repetitions.")
    parser.add_argument("--data", required=False, default=None,
                        help="Data to be sent in the request body in JSON format")
    parser.add_argument("--headers", required=False, default=None,
                        help="Headers to be sent with the request in JSON format")
    parser.add_argument("--port", type=int, default=80, help="Connection port (default is 80)")

    args = parser.parse_args()
    if args.type == "HTTP":
        muninn_socket.main(args.method, args.url, args.data, args.port, args.repeats, args.headers)
    else: 
       muninn_requests.main(args.method, args.url, args.data, args.port, args.repeats, args.headers)