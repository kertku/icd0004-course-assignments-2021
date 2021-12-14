import os
import unittest
from os.path import abspath

from full_weather_report import FullWeatherReport
from helpers.read_and_write_json_file import write_to_json_file, read_json_from_file


class FullWeatherReportTestCase(unittest.TestCase):

    def test_read_city_from_json_file_return_correct_city(self):
        self.assertEqual("Keila", FullWeatherReport().read_city_name_from_file('test/test_data/cities.json'))

    def test_wrong_file_type_rises_system_exit_error(self):
        with self.assertRaises(SystemExit):
            FullWeatherReport().read_city_name_from_file('test/test_data/cities.csv')

    def test_file_not_found_raises_system_exit(self):
        with self.assertRaises(SystemExit):
            FullWeatherReport().read_city_name_from_file('test/test_data/seda_faili_ei_ole.json')

    def test_data_read_from_file_returns_correct_weather_report_output_file_data(self):
        full_weather_report = FullWeatherReport()
        full_weather_report.read_city_name_from_file('test/test_data/cities.json')
        write_to_json_file("pytest_test_file", full_weather_report.show_full_weather_report())
        json_data_from_created_file = read_json_from_file("/output_files/pytest_test_file.json")
        self.assertEqual("Keila", json_data_from_created_file["weatherReportDetails"]["city"])


if __name__ == '__main__':
    unittest.main()
