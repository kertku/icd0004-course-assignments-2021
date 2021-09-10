from greet import Greet
import pytest


class TestClass:

    def test_greet_none_equals_hello_my_friend(self):
        greet_name_none = Greet(None)
        assert greet_name_none.greet(self) == "Hello my friend!"

    def test_greet_empty_string_equals_hello_my_friend(self):
        greet_name_empty_string = Greet("")
        assert greet_name_empty_string.greet(self) == "Hello my friend!"

    def test_greet_uppercase(self):
        greet_name_uppercase = Greet("TIMO")
        assert greet_name_uppercase.greet(self) == "HELLO, TIMO!"

    def test_greet_capitalized_case(self):
        greet_name_capitalized = Greet("Tanel")
        assert greet_name_capitalized.greet(self) == "Hello, Tanel!"

    def test_alternating_case(self):
        greet_name_alternating = Greet("TaNNu")
        assert greet_name_alternating.greet(self) == "Hello, TaNNu!"
