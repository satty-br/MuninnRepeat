#MuninnRepeat - HTTP repeat Attack Tool
```
                                        +-----------------+
                                        |HTTP Request     +--------------------+
                        +-------------->|                 |                    |
                        |               +-----------------+                    v
                        |                                                 +------------+
                        |               +-----------------+               |            |
                        |               |HTTP Request     +-------------->|            |
       +----------------+--------+----->|                 |               |  Website   |
       |                         |      +-----------------+               |            |
(")    |     Muninn              |                                        |            |
/|\ -->|                         |      +-----------------+               +------------+
 |     |                         +----->|HTTP Request     |                ^ ^
/ \    |                         |      |                 +----------------+ |
       +-----------------+-------+      +-----------------+                  |
                         |                                                   |
                         |              +-----------------+                  |
                         |              |HTTP Request     |                  |
                         +------------->|                 +------------------+
                                        +-----------------+
```
MuninnRepeat is a powerful Python-based tool designed to execute HTTP repeat attacks, specifically focusing on repetition-based attacks. It allows users to send custom HTTP requests to a target URL, and if the attack contains a payload, it intelligently holds the last byte and sends it to all repetitions simultaneously.

## Installation
Clone this repository 

```bash
git clone https://github.com/satty-br/MuninnRepeat.git
```

Ensure you have Python 3.x installed on your system.

Install the required dependencies using pip:

```bash
pip install -r requiriments.txt
```

## Usage
To execute a repeat attack using MuninnRepeat, follow the steps below:

```bash
python muninn.py --method METHOD --url URL [--data DATA] [--headers HEADERS] [--port PORT] [--num_requests NUM_REQUESTS]
```

Command-line Arguments
--type Type: using requests or socket.
--method METHOD: The request method (POST, PUT, or DELETE).
--url URL: The target URL for the HTTP request.
--data DATA: (optional) Data to be sent in the request body in JSON format.
--headers HEADERS: (optional) Headers to be sent with the request in JSON format.
--port PORT: (optional) The connection port (default is 80).
--num_requests NUM_REQUESTS: (optional) The number of repeated requests (default is 10).
Examples
Send a POST request with JSON data to https://example.com/api:

```bash
python muninn.py --method POST --url https://example.com/api --data '{"key": "value"}'
```

## Contributing
Contributions to MuninnRepeat are welcome! If you find a bug or have an idea for an improvement, please open an issue or create a pull request on the GitHub repository.

Before contributing, ensure you have read the contribution guidelines.

## License
This project is licensed under the MIT License. See the LICENSE file for details.