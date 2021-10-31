import json
import os
import unittest
from framework.booking_api import BookingApi
from framework.request.booking import Booking
from framework.response.booking_response import BookingResponse
from helper_methods.helper_methods import Helpers
from pathlib import Path


class CreateBookingTests(unittest.TestCase):
    def setUp(self):
        self.booking_payload = Booking().get_fully_payload()
        self.api_response = BookingApi().post_booking(self.booking_payload.toJSON()).content
        self.booking_response = Helpers.JSON_response_to_object(to_class=BookingResponse,
                                                                api_response=self.api_response)

    def test_post_booking_should_return_booking_id(self):
        self.assertTrue(self.booking_response.bookingid is not None)

    def test_post_booking_should_return_correct_booking_person(self):
        self.assertEqual(self.booking_payload.firstname, self.booking_response.booking["firstname"])
        self.assertEqual(self.booking_payload.lastname, self.booking_response.booking["lastname"])

    def test_create_booking_from_file(self):
        file_path = os.path.join(Path.cwd(), "test_data", "jira_54.json")
        booking_payload_from_file = Helpers().load_from_file_to_JSON(file_path=file_path)
        booking = Helpers.JSON_response_to_object(to_class=Booking, api_response=json.dumps(booking_payload_from_file))
        api_response = BookingApi().post_booking(booking.toJSON()).content
        booking_response = Helpers.JSON_response_to_object(to_class=BookingResponse, api_response=api_response)
        self.assertEqual("Tiit", booking_response.booking["firstname"])
        self.assertEqual("Kapp", booking_response.booking["lastname"])

    def test_post_with_wrong_accept_returns_http418(self):
        api_response_status_code = BookingApi().post_booking(self.booking_payload.toJSON(), accept="Vale").status_code
        self.assertEqual(418, api_response_status_code)

    if __name__ == '__main__':
        unittest.main()
