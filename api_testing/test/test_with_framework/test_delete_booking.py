import unittest

from framework.authentication_api import AuthenticationApi
from framework.booking_api import BookingApi
from framework.response.authentication_response import AuthenticationResponse
from helper_methods.helper_methods import Helpers


class DeleteBookingTestCase(unittest.TestCase):

    def setUp(self):
        self.auth_token_api_response = AuthenticationApi().post_authentication(username="admin",
                                                                               password="password123").content
        self.auth_token = Helpers.JSON_response_to_object(to_class=AuthenticationResponse,
                                                          api_response=self.auth_token_api_response).token

    def test_delete_booking_returns_http200(self):
        delete_booking_response = BookingApi().delete_booking(booking_id=2, auth_token=self.auth_token)
        self.assertEqual(201, delete_booking_response.status_code)


if __name__ == '__main__':
    unittest.main()
