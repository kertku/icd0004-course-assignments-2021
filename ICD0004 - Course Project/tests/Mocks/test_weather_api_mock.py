import unittest
from unittest import mock
from unittest.mock import Mock, MagicMock, patch

import self as self

from weather_api import WeatherApi


class TestWeatherApiMock(unittest.TestCase):
    def setUp(self):
        self.patcher = mock.patch('weather_api.WeatherApi.get_current_weather_data', return_value={"name": "Keila"})
        self.patcher.start()

    def test_weather_api_returns_name_when_correct_name_given(self):
        current_weather_report = WeatherApi("Keila")
        current_weather_report.get_current_weather_data()
        self.assertEqual(current_weather_report.get_city_name(), 'Keila')

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
