#What is Inheritance?
#Definition: reuse of attributes and methods from a base class to a derived class.
#Syntax:
class BaseClass:
    def method_base(self) -> None:
        pass # base class method
class DerivedClass(BaseClass):
    def method_derived(self) -> None:
        pass # derived class method



#Inheritance – Basic Example
class Animal:
    def speak(self) -> None:
        print("The animal makes a sound")
class Dog(Animal):
    def bark(self) -> None:
        print("Woof!")
fido:Dog = Dog()
fido.speak() # Output: "The animal makes a sound"
fido.bark() # Output: "Woof!"
#Derived class
#Base class



#Inheritance – super().__init__()/2
# Without super()
class Animal:
    def __init__(self, name:str) -> None:
        self.name:str = name
        print("Animal initialized")
class Dog(Animal):
    def __init__(self, name:str) -> None:
        self.name:str = name
print("Dog initialized")
fido:Dog = Dog("Rudy")
# Output: Dog initialized

# With super()
class Animal:
    def __init__(self, name:str) -> None:
        self.name:str = name  #Parent’s class __init__()
        print("Animal initialized")
class Dog(Animal):
    def __init__(self, name:str) -> None:
        super().__init__(name)
        print("Dog initialized")
fido:Dog = Dog("Rudy")
# Output: Animal initialized
# Dog initialized




#Method Overriding – Basic Example
class Animal:
    def speak(self) -> None:
        print("The animal makes a sound")
class Cat(Animal):
    def speak(self) -> None:
        print("Meow!")
kitty:Cat = Cat()
kitty.speak() # Output: "Meow!"



#Protected Attributes and Methods/2
class Animal:
    def __init__(self) -> None:
        self._type:str = "Mammal" # Protected attribute

    def _sound(self) -> None: # Protected method
        print("Generic animal sound")

class Dog(Animal):
    def describe(self) -> None:
        print(f"I am a {self._type}") # Accessing protected attribute
        self._sound() # Calling protected method
fido:Dog = Dog()
fido.describe() # Output: "I am a Mammal"
# Generic animal sound



