from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HoversPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.hover_page_link = self.driver.find_element(By.LINK_TEXT, "Hovers")
        self.go_to_hovers_page()
        self.all_profiles = self.driver.find_elements(By.XPATH, "//div[@class='figure']")
        self.first_profile = self.all_profiles[0]
        self.second_profile = self.all_profiles[1]
        self.third_profile = self.all_profiles[2]

    def go_to_hovers_page(self):
        self.hover_page_link.click()

    def get_page_title_text(self):
        return self.driver.find_element(By.TAG_NAME, "h3").text

    def get_first_profile(self):
        return self.first_profile

    def get_second_profile(self):
        return self.second_profile

    def get_third_profile(self):
        return self.third_profile

    def hover_over_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def get_profile_user_names(self):
        return self.driver.find_elements(By.TAG_NAME, "h5")

    def profile_link_is_shown(self):
        try:
            return self.driver.find_element(By.LINK_TEXT, "View profile") != ""
        except NoSuchElementException:
            return "No Profile Elements are shown"
