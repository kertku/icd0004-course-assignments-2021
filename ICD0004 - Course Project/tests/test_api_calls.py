from api_caller import ApiCalls


class TestClass:
    APPID = '84e4560ea21a19b05777ab2b8db01083'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

    def test_correct_api_call_returns_status_code_200_OK(self):
        api_call_returns_status_code_200_ok = ApiCalls('Keila', TestClass.BASE_URL, TestClass.APPID)
        assert api_call_returns_status_code_200_ok.get_data_from_api()['cod'] == 200

    def test_api_call_returns_status_code_401_unauthorized(self):
        api_call_with_wrong_api_key = ApiCalls('Keila', TestClass.BASE_URL, '84e')
        assert api_call_with_wrong_api_key.get_data_from_api()['cod'] == 401
