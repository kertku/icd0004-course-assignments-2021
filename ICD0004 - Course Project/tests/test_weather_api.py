import json
import unittest
from weater_api import WeatherApi


class MyTestCase(unittest.TestCase):

    def test_weather_api_returns_name_when_correct_name_given(self):
        current_weather_report = WeatherApi("Keila")
        current_weather_report_to_dictionary = current_weather_report.get_current_weather_data()
        self.assertEqual(current_weather_report_to_dictionary['name'], 'Keila')

    def test_weather_api_returns_404_when_city_name_not_found(self):
        current_weather_report = WeatherApi("Miskimidaeioleolemas")
        current_weather_report_to_dictionary = current_weather_report.get_current_weather_data()
        self.assertEqual(current_weather_report_to_dictionary['cod'], str(404))


if __name__ == '__main__':
    unittest.main()
