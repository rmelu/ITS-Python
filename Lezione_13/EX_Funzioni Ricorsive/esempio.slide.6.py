class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

persona = Person("luca", 30)
print(persona) # Output: Luca, 30 years old




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def __str__(self):
    return f"{self.name}, {self.age} years old"
p = Person("Luca", 30)
print(persona) # Output: Luca, 30 years old
