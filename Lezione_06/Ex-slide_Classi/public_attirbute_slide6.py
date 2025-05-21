#Public Attribute – Basic Example
class Animal:
    def __init__(self) -> None:
        self.name:str = "Generic Animal" # Public attribute
animal:Animal = Animal()
print(animal.name) # Output: "Generic Animal"
animal.name = "It's a dog" # MODIFIES the public attribute 'name'
print(animal.name) # Output: "It's a dog"
#They work.. but are extremely dangerous!


'''#Private Attribute – Basic Example/1
class Animal:
    def __init__(self) -> None:
        self.__name:str = "Generic Animal" # Private attribut
animal:Animal = Animal()
print(animal.name) # Error: not accessible directly
animal.name = "It's a dog" # Creates a NEW public attribute 'name'
print(animal.name) # Output: "It's a dog"
#They no longer work!'''



#Private Attribute – Basic Example/2
class Animal:
    def __init__(self) -> None:
        self.__name:str = "Generic Animal" # Private attribute
# Makes 'name' accessible again
    def get_name(self) -> str:
        return self.__name
animal:Animal = Animal()
print(animal.get_name()) # Output: "Generic Animal"
#They work again!


#Class Attributes – Basic Example
class Person:
    population:int = 0 # Public class attribute
    def __init__(self, name:str) -> None:
        self.__name:str = name # Private attribute
Person.population += 1
print(Person.population) # Output: 0
person1:Person = Person("Alice")
print(Person.population) # Output: 1
person2:Person = Person("Bob")
print(Person.population) # Output: 2


#Static Methods – Basic Example
class Math:
    PI:float = 3.14 # Public class attribute
    @staticmethod
    def circle_area(radius:float) -> float: # Static Method
        return Math.PI * radius * radius
print(Math.PI) # Output: 3.14
print(Math.circle_area(5)) # Output: 78.5


#Class Methods – Basic Example
class Person:
    __population:int = 0 # Private class attribute
    def __init__(self, name:str) -> None:
        self.__name:str = name # Private attribute
        Person.__population += 1
    @classmethod
    def get_population(cls):
        return cls.__population
print(Person.get_population()) # Output: 0
person1:Person = Person("Alice")
print(Person.get_population()) # Output: 1
person2:Person = Person("Bob")
print(Person.get_population()) # Output: 2
person3:Person = Person("riccia")
print(Person.get_population())