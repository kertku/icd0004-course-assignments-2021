import json
import os
import unittest
from unittest import mock
from freezegun import freeze_time

from weather_forcast_report import WeatherForecastReport


class TestForecastDataMock(unittest.TestCase):

    def setUp(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), '../test/test_data/forecast_test_data.json'))
        with open(__location__) as f:
            self.return_value = json.load(f)
        self.patcher = mock.patch('apis.forecast_api.ForecastApi.get_forecast_data_from_api',
                                  return_value=self.return_value)
        self.patcher.start()

    @freeze_time("2021-11-21")
    def test_forecast_first_day_has_correct_data(self):
        weather_forecast = WeatherForecastReport.three_days_forecast("Keila")
        forecast_first_day_pressure = (json.loads(weather_forecast)['forecastReport'][0]['weather']['pressure'])
        self.assertEqual(1006, forecast_first_day_pressure)

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
