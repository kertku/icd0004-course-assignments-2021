import unittest
from framework.authentication_api import AuthenticationApi
from framework.response.authentication_response import AuthenticationResponse
from helper_methods.helper_methods import Helpers


class AuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        self.api_response_correct_login = AuthenticationApi().post_authentication(username="admin",
                                                                                  password="password123")
        self.api_response_invalid_login = AuthenticationApi().post_authentication(username="wrong_user",
                                                                                  password="wrong_password")

    def test_post_correct_authentication_returns_http200(self):
        self.assertEqual(200, self.api_response_correct_login.status_code)

    def test_wrong_credentials_returns_bad_credentials(self):
        authentication_response = Helpers.JSON_response_to_object(to_class=AuthenticationResponse,
                                                                  api_response=self.api_response_invalid_login.content)
        self.assertEqual("Bad credentials", authentication_response.reason)

    def test_authentication_returns_token(self):
        authentication_response = Helpers.JSON_response_to_object(to_class=AuthenticationResponse,
                                                                  api_response=self.api_response_correct_login.content)
        self.assertTrue(authentication_response.token is not None)


if __name__ == '__main__':
    unittest.main()
