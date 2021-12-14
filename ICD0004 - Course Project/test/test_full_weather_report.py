import unittest
from datetime import date, timedelta

from full_weather_report import FullWeatherReport
from helpers.read_and_write_json_file import write_to_json_file, read_json_from_file


class FullWeatherReportTestCase(unittest.TestCase):

    def setUp(self):
        self.full_weather_report = FullWeatherReport()
        self.full_weather_report.read_city_name_from_file('test/test_data/cities.json')
        write_to_json_file("pytest_test_file", self.full_weather_report.show_full_weather_report())
        self.json_data_from_created_file = read_json_from_file("/output_files/pytest_test_file.json")

    def test_read_city_from_json_file_return_correct_city(self):
        self.assertEqual("Keila", FullWeatherReport().read_city_name_from_file('test/test_data/cities.json'))

    def test_wrong_file_type_rises_system_exit_error(self):
        with self.assertRaises(SystemExit):
            FullWeatherReport().read_city_name_from_file('test/test_data/cities.csv')

    def test_file_not_found_raises_system_exit(self):
        with self.assertRaises(SystemExit):
            FullWeatherReport().read_city_name_from_file('test/test_data/seda_faili_ei_ole.json')

    def test_data_read_from_file_returns_correct_weather_report_output_file_data(self):
        self.assertEqual("Keila", self.json_data_from_created_file["weatherReportDetails"]["city"])

    # Todo Test fails if itś run on evening, where there are no more today's date! FIX IT
    def test_data_read_from_file_returns_correct_weather_forecast_dates_to_output_file_data(self):
        [self.assertEqual((date.today() + timedelta(days=i)).strftime("%Y-%m-%d"),
                          self.json_data_from_created_file["forecastReport"][i]["date"]) for i in range(3)]

    def test_current_weather_report_from_full_report_file_returns_correct_date(self):
        current_weather_report_date = self.json_data_from_created_file["currentWeatherReport"]["date"]
        date_time_today = date.today().strftime("%Y-%m-%d")
        self.assertEqual(date_time_today, current_weather_report_date)

    def test_file_read_with_multiple_cities_returns_correct_list_with_city_names(self):
        self.assertEqual(["Keila", "Tapa", "Tallinn"],
                         FullWeatherReport().read_city_names_from_file("test/test_data/multiple_cities.json"))


if __name__ == '__main__':
    unittest.main()
