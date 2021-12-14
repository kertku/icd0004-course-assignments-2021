import json
import os
import unittest
from os.path import abspath
from unittest import mock


class BaseTestWithFileSetupTestCase(unittest.TestCase):
    def setUp(self):
        location = os.path.join(abspath(os.path.dirname(__file__)), "../test_data/forecast_test_data.json")
        with open(location) as f:
            self.return_value = json.load(f)
        self.patcher = mock.patch('apis.forecast_api.ForecastApi.get_forecast_data_from_api',
                                  return_value=self.return_value)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

if __name__ == '__main__':
    unittest.main()
