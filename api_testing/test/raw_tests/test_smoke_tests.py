import json
import unittest
import requests


class SmokeTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://restful-booker.herokuapp.com/booking"

    def test_get_booking_should_return_200(self):
        response = requests.get(self.base_url)
        self.assertEqual(200, response.status_code, "Should return 200")

    def test_get_booking_by_id_should_return_200(self):
        response = requests.get(self.base_url + "/11")
        self.assertEqual(200, response.status_code, "Should return 200")

    def test_post_booking_should_return_http200(self):
        post_object = {
            "firstname": "Raimond",
            "lastname": "Valge",
            "totalprice": 900,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2021-02-23",
                "checkout": "2022-03-23"
            },
            "additionalneeds": "Full service needed!"
        }
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.post(self.base_url, data=json.dumps(post_object), headers=headers)
        self.assertEqual(200, response.status_code, "Post should return http200")


if __name__ == '__main__':
    unittest.main()
