import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_base_test_setup import BaseTestCase


class HomePageTestCase(BaseTestCase):

    def test_can_open_homepage(self):
        web_page_title_element = self.driver.find_element(By.CLASS_NAME, "heading")
        self.assertEqual("Welcome to the-internet", web_page_title_element.text)


if __name__ == '__main__':
    unittest.main()
