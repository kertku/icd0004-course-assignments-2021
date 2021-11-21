import unittest

from selenium.webdriver.common.by import By

from test.test_base_test_setup import BaseTestCase


class FormAuthenticationTestCase(BaseTestCase):

    def setUp(self):
        super(FormAuthenticationTestCase, self).setUp()
        form_authentication_link = self.driver.find_element(By.LINK_TEXT, "Form Authentication")
        form_authentication_link.click()

    def test_can_open_form_authentication_page(self):
        h2_element = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual("Login Page", h2_element.text)

    def test_should_login_to_secure_area_with_valid_credentials(self):
        valid_username = "tomsmith"
        valid_password = "SuperSecretPassword!"
        self.driver.find_element(By.ID, "username").send_keys(valid_username)
        self.driver.find_element(By.ID, "password").send_keys(valid_password)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        secure_area_title_element = self.driver.find_element(By.TAG_NAME, "h2").text
        self.assertEqual("Secure Area", secure_area_title_element)

    def test_should_not_login_to_secure_area_with_invalid_credentials(self):
        valid_username = "vale"
        valid_password = "kasutaja"
        self.driver.find_element(By.ID, "username").send_keys(valid_username)
        self.driver.find_element(By.ID, "password").send_keys(valid_password)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        flash_element = self.driver.find_element(By.ID, "flash").text.rstrip("\n×")
        self.assertEqual("Your username is invalid!", flash_element)


if __name__ == '__main__':
    unittest.main()
