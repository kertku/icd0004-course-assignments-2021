import unittest
import unittest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import firefox
from selenium.webdriver.common.by import By


class BaseTestCase(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
