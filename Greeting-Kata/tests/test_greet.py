from greet import Greet
import pytest


class TestClass:

    def test_greet_none_equals_hello_my_friend(self):
        greet_name_none = Greet(None)
        assert greet_name_none.greet() == "Hello my friend!"

    def test_greet_empty_string_equals_hello_my_friend(self):
        greet_name_empty_string = Greet("")
        assert greet_name_empty_string.greet() == "Hello my friend!"

    def test_greet_uppercase(self):
        greet_name_uppercase = Greet("TIMO")
        assert greet_name_uppercase.greet() == "HELLO, TIMO!"

    def test_greet_capitalized_case(self):
        greet_name_capitalized = Greet("Tanel")
        assert greet_name_capitalized.greet() == "Hello, Tanel."

    def test_alternating_case(self):
        greet_name_alternating = Greet("TaNNu")
        assert greet_name_alternating.greet() == "Hello, TaNNu."

    def test_two_names_from_list(self):
        greet_two_names_from_list = Greet(["Jill", "Jane"])
        assert greet_two_names_from_list.greet() == "Hello, Jill and Jane."

    def test_arbitrary_numbers_of_names(self):
        arbitrary_numbers_of_names = Greet(["Amy", "Brian", "Charlotte"])
        assert arbitrary_numbers_of_names.greet() == "Hello, Amy, Brian and Charlotte."

    def test_mixed_of_normal_and_shouted_names(self):
        mixed_of_normal_and_shouted_names = Greet(["Amy", "BRIAN", "Charlotte"])
        assert mixed_of_normal_and_shouted_names.greet() == "Hello, Amy and Charlotte. AND HELLO, BRIAN!"

    def test_mixed_of_normal_and_shouted_names_with_two_upper_case_names(self):
        mixed_of_normal_and_shouted_names_two_upper_case = Greet(["Amy", "BRIAN", "Charlotte", "TIIT"])
        assert mixed_of_normal_and_shouted_names_two_upper_case.greet(
            ) == "Hello, Amy and Charlotte. AND HELLO, BRIAN AND TIIT."

    def test_entries_contains_commas(self):
        entries_contains_commas = Greet(["Bob", "Charlie, Dianne"])
        assert entries_contains_commas.greet() == "Hello, Bob, Charlie and Dianne."

    def test_input_to_escape_intentional_commas(self):
        test_input_to_escape_intentional_commas = Greet(["Bob", "\"Charlie, Dianne\""])
        assert test_input_to_escape_intentional_commas.greet() == "Hello, Bob, Charlie and Dianne."

    def test_array_input_with_one_name_lower_case(self):
        array_input_with_one_name_lower_case = Greet(["Bob"])
        assert array_input_with_one_name_lower_case.greet() == "Hello, Bob.", "Should be Hello, Bob."

    def test_array_input_with_one_name_upper_case(self):
        array_input_with_one_name_upper_case = Greet(["DIANE"])
        assert array_input_with_one_name_upper_case.greet() == "HELLO, DIANE!"
