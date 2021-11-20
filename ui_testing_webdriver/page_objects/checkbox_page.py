from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CheckBoxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.checkboxes_link = self.driver.find_element(By.LINK_TEXT, "Checkboxes")
        self.go_to_page()
        self.checkbox_1 = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        self.checkbox_2 = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
        self.all_checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    def get_page_title_text(self):
        return self.driver.find_element(By.TAG_NAME, "h3").text

    def go_to_page(self):
        self.checkboxes_link.click()

    def click_element_checkbox_1(self):
        self.checkbox_1.click()

    def click_element_checkbox_2(self):
        self.checkbox_2.click()

    def is_checkbox_2_checked(self):
        return self.checkbox_2.is_selected()

    def is_checkbox_1_checked(self):
        return self.checkbox_1.is_selected()

    def check_all_checkboxes(self):
        for checkbox in self.all_checkboxes:
            if not checkbox.is_selected():
                checkbox.click()

    def deselect_all_checkboxes(self):
        for checkbox in self.all_checkboxes:
            if checkbox.is_selected():
                checkbox.click()
