import unittest
from unittest import mock
from unittest.mock import Mock, MagicMock, patch

from weather_api import WeatherApi


class TestWeatherApiMock(unittest.TestCase):

    @patch('weather_api.WeatherApi.get_current_weather_data')
    def test_weather_api_returns_name_when_correct_name_given(self, mock_get_data_from_api):
        mock_get_data_from_api.return_value = {"name": "Keila"}
        current_weather_report = WeatherApi("Keila")
        current_weather_report.get_current_weather_data()
        self.assertEqual(current_weather_report.get_city_name(), 'Keila')


if __name__ == '__main__':
    unittest.main()
