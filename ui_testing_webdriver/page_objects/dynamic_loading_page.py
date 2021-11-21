from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class DynamicLoadingPage(BasePage):
    def get_page_title_text(self):
        return self.driver.find_element(By.TAG_NAME, "h3").text

    def go_to_page(self):
        self.driver.find_element(By.LINK_TEXT, "Dynamic Loading").click()


