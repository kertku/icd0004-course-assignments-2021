class Greet:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def say_hello_with_one_name(name):
        if name.isupper():
            return "HELLO, %s!" % name
        else:
            return "Hello, %s!" % name

    @staticmethod
    def say_hello_with_multiple_names_lower_case(names):
        greeting = "Hello"
        for name in names:
            if name is names[-1]:
                greeting += (" and %s." % name)
            else:
                greeting += ", %s" % name
        return greeting

    def say_hello_with_multiple_names(self, name):
        greeting = ""
        upper_case_names = []
        lower_case_names = []
        for i in self.name:
            if i.isupper():
                upper_case_names.append(i)
            else:
                lower_case_names.append(i)
        if len(lower_case_names) <= 1:
            greeting = self.say_hello_with_one_name(lower_case_names[0])
        else:
            greeting = self.say_hello_with_multiple_names_lower_case(lower_case_names)
        if len(upper_case_names) == 0:
            return greeting
        elif len(upper_case_names) <= 1:
            greeting += " AND "
            greeting += self.say_hello_with_one_name(upper_case_names[0])
        else:
            greeting += " AND "
            greeting += (self.say_hello_with_multiple_names_lower_case(upper_case_names)).upper()

        return greeting

    def greet(self, name):
        if self.name is None or self.name == "":
            return "Hello my friend!"
        if isinstance(self.name, str):
            return self.say_hello_with_one_name(self.name)
        if isinstance(self.name, list):
            return self.say_hello_with_multiple_names(self.name)
        else:
            return "Wrong input"
