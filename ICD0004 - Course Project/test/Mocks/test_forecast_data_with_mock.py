import json
import unittest
from unittest import mock

from weather_forcast_report import WeatherForecastReport


class TestForecastDataMock(unittest.TestCase):
    def setUp(self):
        with open('../test_data/forecast_test_data.json') as f:
            self.return_value = json.load(f)
        self.patcher = mock.patch('apis.weather_api.WeatherApi.get_current_weather_data_from_api',
                                  return_value=self.return_value)
        self.patcher.start()

    def test_forecast_first_day_has_correct_data(self):
        weather_forecast = WeatherForecastReport.three_days_forecast("Keila")
        forecast_first_day_pressure = (json.loads(weather_forecast)['forecastReport'][0]['weather']['pressure'])
        self.assertEqual(1006, forecast_first_day_pressure)

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
