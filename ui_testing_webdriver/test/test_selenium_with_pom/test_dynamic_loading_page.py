import unittest
from page_objects.dynamic_loading_page import DynamicLoadingPage
from test.test_base_test_setup import BaseTestCase


class DynamicLoadingPageTestCase(BaseTestCase):
    def setUp(self):
        super(DynamicLoadingPageTestCase, self).setUp()
        self.dynamic_loading_page = DynamicLoadingPage(self.driver)

    def test_get_dynamic_loading_page_title(self):
        self.dynamic_loading_page.go_to_page()
        self.assertEqual("Dynamically Loaded Page Elements", self.dynamic_loading_page.get_page_title_text())


if __name__ == '__main__':
    unittest.main()
