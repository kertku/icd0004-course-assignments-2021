import unittest

from full_weather_report import FullWeatherReport
from helpers import date_converter
from helpers.read_and_write_json_file import write_to_json_file
from helpers.file_operations import if_file_exists_then_delete_file, absolute_file_path


class HelpersTestCase(unittest.TestCase):
    def test_date_converter_returns_correct_format(self):
        self.unix_timestamp = date_converter.convert_unix_dateformat_to_utc(1284101485)
        self.correct_format = "2010-09-10"
        self.assertEqual(self.unix_timestamp, self.correct_format)

    def test_correct_log_message_when_new_file_created(self):
        data = {"testdata": "testdata"}
        log_message = write_to_json_file("test_output", data, output_dir="test/test_data/test_output_files")
        self.assertEqual("test_output.json in output_files folder already exists! File overridden!", log_message)

    def test_correct_log_message_when_file_is_overridden(self):
        file_path = absolute_file_path('/test/test_data/test_output_files/test_output_override.json')
        if_file_exists_then_delete_file(file_path)
        data = {"testdata": "testdata"}
        log_message = write_to_json_file("test_output_override", data,
                                         output_dir="test/test_data/test_output_files")
        self.assertEqual("New file: test_output_override.json created to output_files folder!", log_message)

    def test_write_to_json_with_unknown_file_name_returns_error(self):
        unknown_city_name = FullWeatherReport()
        unknown_city_name.read_city_name_from_file('test/test_data/uncorrect_city_name.json')
        unknown_city_name_report_result = unknown_city_name.show_full_weather_report()
        return_result = write_to_json_file(f"{unknown_city_name.city_name}", unknown_city_name_report_result)
        self.assertEqual("Suvaline linn.json not created. No data for this city!", return_result)


if __name__ == '__main__':
    unittest.main()
