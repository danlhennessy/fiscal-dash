import unittest
from tests.test_flask import FlaskTestCase


def hello_world():
    return 'Hello, World!'


class HelloWorldTestCase(unittest.TestCase):

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, 'Hello, World!')


if __name__ == "__main__":
    unittest.main()
