class Greet:
    def __init__(self, name):
        self.name = name

    def greet(self, name):
        if self.name is None or self.name == "":
            return "Hello my friend!"
        if isinstance(self.name, str):
            if self.name.isupper():
                return "HELLO, %s!" % self.name
            else:
                return "Hello, %s!" % self.name
        if isinstance(self.name, list):
            greeting = "Hello, "
            for name in self.name:
                if name is self.name[-1]:
                    greeting += (" and %s." % name)
                else:
                    greeting += name
            return greeting
        else:
            return "Wrong input"
