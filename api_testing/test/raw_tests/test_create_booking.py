import json
import unittest
import requests


class TestCreateBooking(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://restful-booker.herokuapp.com/booking"
        self.post_object = {
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
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        self.response = requests.post(self.base_url, data=json.dumps(self.post_object), headers=self.headers)

    def test_post_booking_should_return_booking_id(self):
        response_booking_id = self.response.json()["bookingid"]
        self.assertTrue(self.response.status_code == 200 and response_booking_id is not None)

    def test_post_booking_should_return_correct_booking_person(self):
        response_firstname = self.response.json()["booking"]["firstname"]
        response_lastname = self.response.json()["booking"]["lastname"]
        self.assertTrue("Raimond" == response_firstname and "Valge" == response_lastname)


if __name__ == '__main__':
    unittest.main()
