from api_caller import ApiCaller


class TestClass:
    APPID = '84e4560ea21a19b05777ab2b8db01083'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

    def test_correct_api_call_returns_status_code_200_OK(self):
        api_call_returns_status_code_200_ok = ApiCaller('Keila', TestClass.BASE_URL, TestClass.APPID)
        assert api_call_returns_status_code_200_ok.get_data_from_api()['cod'] == 200

    def test_api_call_with_wrong_AppID_returns_status_code_401_unauthorized(self):
        api_call_with_wrong_api_key = ApiCaller('Keila', TestClass.BASE_URL, '84e')
        assert api_call_with_wrong_api_key.get_data_from_api()['cod'] == 401

    def test_incorrect_name_api_call_returns_status_code_404(self):
        api_call_returns_status_code_404 = ApiCaller('NotCorrect', TestClass.BASE_URL, TestClass.APPID)
        assert api_call_returns_status_code_404.get_data_from_api()['cod'] == str(404)

    def test_API_should_return_city_name_when_name_is_given(self):
        api_call_returns_city_name = ApiCaller('Keila', TestClass.BASE_URL, TestClass.APPID)
        assert api_call_returns_city_name.get_data_from_api()['name'] == str("Keila")

    def test_API_should_return_lat_and_lon_properties(self):
        api_has_lat_lon_properties = ApiCaller('Keila', TestClass.BASE_URL, TestClass.APPID)
        assert ('lat' and 'lon' in (api_has_lat_lon_properties.get_data_from_api()['coord'])) is True
