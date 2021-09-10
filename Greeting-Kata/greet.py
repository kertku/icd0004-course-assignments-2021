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
            print("Hello ")
            for i in self.name:
                if i is self.name[-1]:
                    print("and " + i)
                else:
                    print(i + ", ")