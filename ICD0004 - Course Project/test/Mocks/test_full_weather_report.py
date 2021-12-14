import unittest

from full_weather_report import FullWeatherReport
from helpers.read_and_write_json_file import write_to_json_file, read_json_from_file
from test.Mocks.test_base_test_with_file_setup import BaseTestWithFileSetupTestCase


class FullWeatherReportWithMockTestCase(BaseTestWithFileSetupTestCase):
    def setUp(self):
        super(FullWeatherReportWithMockTestCase, self).setUp()

    def test_data_read_from_file_returns_correct_weather_report_output_file_data_city_name(self):
        full_weather_report = FullWeatherReport()
        full_weather_report.read_city_name_from_file('test/test_data/cities.json')
        write_to_json_file("pytest_test_file", full_weather_report.show_full_weather_report())
        json_data_from_created_file = read_json_from_file("/output_files/pytest_test_file.json")
        self.assertEqual("Keila", json_data_from_created_file["weatherReportDetails"]["city"])

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
