import unittest

from helpers import date_converter


class HelpersTestCase(unittest.TestCase):
    def test_date_converter_returns_correct_format(self):
        self.unix_timestamp = date_converter.convert_unix_dateformat_to_utc(1284101485)
        self.correct_format = "2010-09-10"
        self.assertEqual(self.unix_timestamp, self.correct_format)  # add assertion here


if __name__ == '__main__':
    unittest.main()
