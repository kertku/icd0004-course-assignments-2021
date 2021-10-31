import unittest
from framework.authentication_api import AuthenticationApi
from framework.booking_api import BookingApi
from framework.request.booking import Booking
from framework.response.authentication_response import AuthenticationResponse
from helper_methods.helper_methods import Helpers


class PutBookingTestCase(unittest.TestCase):
    def setUp(self):
        self.auth_token_api_response = AuthenticationApi().post_authentication(username="admin",
                                                                               password="password123").content
        self.auth_token = Helpers.JSON_response_to_object(to_class=AuthenticationResponse,
                                                          api_response=self.auth_token_api_response).token

    def test_put__booking_should_return_http200(self):
        booking_payload = Booking().get_fully_payload()
        api_response_status_code = BookingApi().put_booking(booking_id=1, auth_token=self.auth_token,
                                                            booking_payload=booking_payload.toJSON()).status_code
        self.assertEqual(200, api_response_status_code)


if __name__ == '__main__':
    unittest.main()
