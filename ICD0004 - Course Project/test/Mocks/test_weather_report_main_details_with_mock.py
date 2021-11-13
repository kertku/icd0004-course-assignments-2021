import json
import unittest
from unittest import mock
from weather_api import WeatherApi
from weather_report_main_details import WeatherReportDetails


class TestWeatherReportDetailsMock(unittest.TestCase):
    def setUp(self):
        self.patcher = mock.patch('weather_api.WeatherApi.get_current_weather_data',
                                  return_value={"name": "Keila", "coord": {"lon": 35, "lat": 65}})
        self.weather_api = WeatherApi("Keila")
        self.weather_report_details = WeatherReportDetails()
        self.patcher.start()

    def test_correct_weather_report_details_coord_response(self):
        self.weather_report_details.parse_json_result_to_weather_report_details(
            self.weather_api.get_current_weather_data())
        assert self.weather_report_details.get_coordinates() == "65,35"

    def test_correct_weather_report_city_name_coord_response(self):
        self.weather_report_details.parse_json_result_to_weather_report_details(
            self.weather_api.get_current_weather_data())
        assert self.weather_report_details.get_city_name() == "Keila"

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
