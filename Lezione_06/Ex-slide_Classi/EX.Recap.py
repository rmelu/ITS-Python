class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Ciao mi chiamo {self.name} e ho {self.age} anni. ")

alice = Persona("Alice", 30)
bob = Persona("Bob", 34)

print(alice.name)
bob.say_hello()