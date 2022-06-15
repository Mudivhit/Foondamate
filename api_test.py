import unittest
import requests


class MyTestCase(unittest.TestCase):

    def test_status_code(self):
        response = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
        self.assertEqual(200, response.status_code)

    def test_content_type(self):
        response = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
        self.assertIn("application/json", response.headers["Content-Type"])


if __name__ == '__main__':
    unittest.main()
