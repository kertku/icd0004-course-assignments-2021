import json
import unittest


from test.Mocks.test_base_test_with_file_setup import BaseTestWithFileSetupTestCase
from weather_forcast_report import WeatherForecastReport


class TestForecastDataMock(BaseTestWithFileSetupTestCase):
    def setUp(self):
        super(TestForecastDataMock, self).setUp()
        self.three_days_forecast = json.loads(WeatherForecastReport().three_days_forecast("Keila"))
        self.first_day_forecast = self.three_days_forecast['forecastReport'][0]
        self.second_day_forecast = self.three_days_forecast['forecastReport'][1]
        self.third_day_forecast = self.three_days_forecast['forecastReport'][2]

    def test_third_day_forecast_has_correct_average_pressures(self):
        self.assertEqual(1006, self.first_day_forecast['weather']['pressure'], "First day pressure should be 1006")
        self.assertEqual(1013, self.second_day_forecast['weather']['pressure'], "Second day pressure should be 1013")
        self.assertEqual(1010, self.third_day_forecast['weather']['pressure'], "Third day pressure should be 1010")

    def test_third_day_forecast_has_correct_average_temperatures(self):
        self.assertEqual(0, self.first_day_forecast['weather']['temperature'], "First day temperature should be 0")
        self.assertEqual(0, self.second_day_forecast['weather']['temperature'], "Second day temperature should be 0")
        self.assertEqual(1, self.third_day_forecast['weather']['temperature'], "Third day temperature should be 1")

    def test_third_day_forecast_has_correct_average_humidity_values(self):
        self.assertEqual(66, self.first_day_forecast['weather']['humidity'], "First day humidity should be 66")
        self.assertEqual(70, self.second_day_forecast['weather']['humidity'], "Second day humidity should be 70")
        self.assertEqual(89, self.third_day_forecast['weather']['humidity'], "Third day humidity should be 89")

    def test_third_day_forecast_has_correct_dates(self):
        self.assertEqual('2021-11-21', self.first_day_forecast['date'], "First day date should be 2021-11-21")
        self.assertEqual('2021-11-22', self.second_day_forecast['date'], "Second day date should be 2021-11-22")
        self.assertEqual('2021-11-23', self.third_day_forecast['date'], "Third day date should be 2021-11-23")

    def tearDown(self):
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
