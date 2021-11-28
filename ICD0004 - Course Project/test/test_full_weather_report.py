import unittest

from full_weather_report import FullWeatherReport


class FullWeatherReportTestCase(unittest.TestCase):

    def test_read_city_from_json_file_return_correct_city(self):
        self.assertEqual("Keila", FullWeatherReport().read_city_name_from_file('test/test_data/cities.json'))

    def test_wrong_file_name_raises_file_not_found_exception(self):
        with self.assertRaises(FileNotFoundError):
            FullWeatherReport().read_city_name_from_file('test/test_data/wrong_name.json')

    def test_wrong_file_type_rises_type_error(self):
        with self.assertRaises(TypeError):
            FullWeatherReport().read_city_name_from_file('test/test_data/cities.csv')


if __name__ == '__main__':
    unittest.main()
