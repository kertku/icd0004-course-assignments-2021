import os
import unittest
from os.path import abspath

from full_weather_report import FullWeatherReport


class FullWeatherReportTestCase(unittest.TestCase):

    def test_read_city_from_json_file_return_correct_city(self):
        self.assertEqual("Keila", FullWeatherReport().read_city_name_from_file('test/test_data/cities.json'))

    def test_wrong_file_type_rises_system_exit_error(self):
        with self.assertRaises(SystemExit):
            FullWeatherReport().read_city_name_from_file('test/test_data/cities.csv')

    def test_file_not_found_raises_system_exit(self):
        with self.assertRaises(SystemExit):
            FullWeatherReport().read_city_name_from_file('test/test_data/seda_faili_ei_ole.json')


if __name__ == '__main__':
    unittest.main()
