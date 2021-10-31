import unittest
from framework.booking_api import BookingApi
from framework.request.booking import Booking


class SmokeTestsWithFramework(unittest.TestCase):

    def setUp(self):
        self.booking_api = BookingApi()

    def test_get_booking_should_return_200(self):
        self.assertEqual(200, self.booking_api.get_bookings().status_code)

    def test_get_booking_by_id_should_return_200(self):
        self.assertEqual(200, self.booking_api.get_booking_by_id(1).status_code)

    def test_post_booking_should_return_http200(self):
        booking_payload = Booking().get_fully_payload()
        self.assertEqual(200, self.booking_api.post_booking(booking_payload.toJSON()).status_code)

    if __name__ == '__main__':
        unittest.main()
