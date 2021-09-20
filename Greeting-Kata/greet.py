class Greet:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def say_hello_with_one_name(name):
        greeting = f"Hello, {name}."
        if name.isupper():
            return f"HELLO, {name}!"
        else:
            return greeting

    @staticmethod
    def split_names_with_commas(names):
        names_list = []
        for i in names:
            spliced_name = i.strip(""""\"""").split(", ")
            for j in spliced_name:
                names_list.append(j)
        return names_list

    @staticmethod
    def say_hello_with_multiple_names_lower_case(names):
        greeting = "Hello"
        for name in names:
            if name is names[-1]:
                greeting += f" and {name}."
            else:
                greeting += f", {name}"
        return greeting

    def say_hello_with_multiple_names(self):
        upper_case_names = []
        lower_case_names = []
        self.name = self.split_names_with_commas(self.name)
        for name in self.name:
            if name.isupper():
                upper_case_names.append(name)
            else:
                lower_case_names.append(name)
        if len(lower_case_names) == 0:
            return self.say_hello_with_one_name(upper_case_names[0])
        elif len(lower_case_names) <= 1:
            greeting = self.say_hello_with_one_name(lower_case_names[0])
        else:
            greeting = self.say_hello_with_multiple_names_lower_case(lower_case_names)
        if len(upper_case_names) == 0:
            return greeting
        elif len(upper_case_names) == 1:
            greeting += f" AND {self.say_hello_with_one_name(upper_case_names[0])}"
        else:
            greeting += f" AND {(self.say_hello_with_multiple_names_lower_case(upper_case_names)).upper()}"
        return greeting

    def greet(self):
        if self.name is None or self.name == "":
            return "Hello my friend!"
        if isinstance(self.name, str):
            return self.say_hello_with_one_name(self.name)
        if isinstance(self.name, list):
            return self.say_hello_with_multiple_names()
        else:
            return "Wrong input"
