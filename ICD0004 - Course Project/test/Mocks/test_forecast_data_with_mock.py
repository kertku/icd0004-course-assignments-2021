import json
import os
import unittest
from os.path import abspath
from unittest import mock

from apis.forecast_api import ForecastApi
from weather_forcast_report import WeatherForecastReport


class TestForecastDataMock(unittest.TestCase):
    def setUp(self):
        location = os.path.join(abspath(os.path.dirname(__file__)), "../test_data/forecast_test_data.json")
        with open(location) as f:
            self.return_value = json.load(f)
        self.patcher = mock.patch('apis.forecast_api.ForecastApi.get_forecast_data_from_api',
                                  return_value=self.return_value)
        self.patcher.start()

    def test_third_day_forecast_has_correct_average_pressures(self):
        print(ForecastApi("Keila").json_to_pandas_dataframe())
        print(WeatherForecastReport().three_days_forecast("Keila"))
        self.assertEqual(1012, 1123)

    def test_third_day_forecast_has_correct_average_temperatures(self):
        return NotImplemented

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
