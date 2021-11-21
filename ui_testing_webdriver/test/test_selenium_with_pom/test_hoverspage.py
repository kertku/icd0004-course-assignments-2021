import unittest
from page_objects.hovers_page import HoversPage
from test.test_base_test_setup import BaseTestCase


class HoversTestCase(BaseTestCase):
    def setUp(self):
        super(HoversTestCase, self).setUp()
        self.hovers_page = HoversPage(self.driver)

    def test_get_hovers_page_title(self):
        self.assertEqual("Hovers", self.hovers_page.get_page_title_text())

    def test_if_not_hovered_over_all_profiles_does_not_show_name(self):
        for profile in self.hovers_page.get_profile_user_names():
            self.assertTrue(profile .text == "")
            self.assertEqual("No Profile Elements are shown", self.hovers_page.profile_link_is_shown())

    def test_first_profile_shows_name_when_hovered_over(self):
        self.hovers_page.hover_over_element(self.hovers_page.get_first_profile())
        self.assertEqual("name: user1", self.hovers_page.get_profile_user_names()[0].text)
        self.assertTrue(self.hovers_page.profile_link_is_shown())

    def test_second_profile_shows_name_when_hovered_over(self):
        self.hovers_page.hover_over_element(self.hovers_page.get_second_profile())
        self.assertEqual("name: user2", self.hovers_page.get_profile_user_names()[1].text)
        self.assertTrue(self.hovers_page.profile_link_is_shown())

    def test_third_profile_shows_name_when_hovered_over(self):
        self.hovers_page.hover_over_element(self.hovers_page.get_third_profile())
        self.assertEqual("name: user3", self.hovers_page.get_profile_user_names()[2].text)
        self.assertTrue(self.hovers_page.profile_link_is_shown())


if __name__ == '__main__':
    unittest.main()
