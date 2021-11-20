import unittest
from page_objects.checkbox_page import CheckBoxPage
from test.test_base_test_setup import BaseTestCase


class CheckBoxPageTestCase(BaseTestCase):

    def setUp(self):
        super(CheckBoxPageTestCase, self).setUp()
        self.checkbox_page = CheckBoxPage(self.driver)

    def test_get_checkbox_page_title(self):
        self.assertEqual("Checkboxes", self.checkbox_page.get_page_title_text())

    def test_can_select_all_checkboxes(self):
        self.checkbox_page.check_all_checkboxes()
        self.assertTrue(self.checkbox_page.is_checkbox_1_checked())
        self.assertTrue(self.checkbox_page.is_checkbox_2_checked())

    def test_can_deselect_all_checkboxes(self):
        self.checkbox_page.deselect_all_checkboxes()
        self.assertFalse(self.checkbox_page.is_checkbox_1_checked())
        self.assertFalse(self.checkbox_page.is_checkbox_2_checked())


if __name__ == '__main__':
    unittest.main()
