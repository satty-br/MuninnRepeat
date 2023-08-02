import unittest
from muninn_requests import main, parse_data

class TestCustomHTTPRequest(unittest.TestCase):
    def test_parse_data_with_data(self):
        data = "{'key': 'value'}"
        domain = "example.com"
        endpoint = "/api"
        method = "POST"
        request_body, last_character = parse_data(
            domain, endpoint, method, data)
        expected_body = "POST /api HTTP/1.1\r\nHost: example.com\r\nContent-Type: application/json\r\nContent-Length: 15\r\n\r\n{'key': 'value'}"
        self.assertEqual(request_body, expected_body)
        self.assertEqual(last_character, "'")

    def test_parse_data_without_data(self):
        domain = "example.com"
        endpoint = "/api"
        method = "GET"
        request_body, last_character = parse_data(
            domain, endpoint, method, None)
        expected_body = "GET /api HTTP/1.1\r\nHost: example.com\r\n"
        self.assertEqual(request_body, expected_body)
        self.assertIsNone(last_character)

    def test_main_with_valid_arguments(self):
        method = "POST"
        url = "https://example.com/api"
        data = '{"key": "value"}'
        port = 443
        num_requests = 5

        # Ensure main function runs without errors
        try:
            main(method, url, data, port, num_requests)
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

    def test_main_with_invalid_url(self):
        method = "GET"
        url = "invalid_url"
        data = None
        port = 80
        num_requests = 3

        # Ensure main function raises an exception for an invalid URL
        with self.assertRaises(Exception) as context:
            main(method, url, data, port, num_requests)
        self.assertTrue("Invalid URL" in str(context.exception))

    def test_main_with_invalid_method(self):
        method = "INVALID_METHOD"
        url = "https://example.com/api"
        data = None
        port = 80
        num_requests = 1

        # Ensure main function raises an exception for an invalid method
        with self.assertRaises(Exception) as context:
            main(method, url, data, port, num_requests)
        self.assertTrue("Invalid method" in str(context.exception))

    def test_main_with_data_and_invalid_last_character(self):
        method = "PUT"
        url = "https://example.com"
        data = "some data without newline"
        port = 443
        num_requests = 2

        # Ensure main function raises an exception for invalid data with no newline at the end
        with self.assertRaises(Exception) as context:
            main(method, url, data, port, num_requests)
        self.assertTrue("Invalid data format" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
