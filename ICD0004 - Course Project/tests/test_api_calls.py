import pytest
from api_caller import ApiCalls


class TestClass:

    def test_api_call_returns_status_code_200_OK(self):
        api_call_returns_status_code_200_ok = ApiCalls('Keila', 'https://api.openweathermap.org/data/2.5/weather?',
                                                       '84e4560ea21a19b05777ab2b8db01083')
        assert api_call_returns_status_code_200_ok.get_data_from_api()[1] == 200

    def test_api_call_returns_status_code_401_unauthorized(self):
        api_call_with_wrong_api_key = ApiCalls('Keila', 'https://api.openweathermap.org/data/2.5/weather?',
                                               '84e')
        assert api_call_with_wrong_api_key.get_data_from_api()[1] == 401
