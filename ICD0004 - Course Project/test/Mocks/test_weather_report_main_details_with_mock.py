import unittest
from unittest import mock
from apis.weather_api import WeatherApi
from weather_report_main_details import WeatherReportDetails


class TestWeatherReportDetailsMock(unittest.TestCase):
    def setUp(self):
        self.patcher = mock.patch('apis.weather_api.WeatherApi.get_current_weather_data_from_api',
                                  return_value={"name": "Keila", "coord": {"lon": 35, "lat": 65}})
        self.weather_api = WeatherApi("Keila")
        self.patcher.start()
        self.weather_api = self.weather_api.get_current_weather_data_from_api()
        self.weather_report_details = WeatherReportDetails(self.weather_api)

    def test_correct_weather_report_details_coord_response(self):
        self.weather_report_details.parse_json_result_to_weather_report_details()
        assert self.weather_report_details.get_coordinates() == "65,35"

    def test_correct_weather_report_city_name_coord_response(self):
        self.weather_report_details.parse_json_result_to_weather_report_details()
        assert self.weather_report_details.get_city_name() == "Keila"

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
