'''What is Lambda in Python?
A lambda is a tiny function useful when you want to define a function with quick and simple logic.
Often, the lambda function is defined as the argument to other functions.
Syntax:
lambda arguments: expression
How does it work?
A lambda:
• can have any number of arguments, but
• must have only one expression, which gets returned automatically.'''


'''
Typing the lambda
What is Callable?
• Callable is a type hint from the typing module used to specify that a variable is a function.
General form:
from typing import Callable
Callable[[ArgType1, ArgType2, ...], ReturnType]'''

#Example:
from typing import Callable
# Function that takes two ints and returns an int
multiply: Callable[[int, int], int] = lambda a, b: a * b
print(multiply(5, 10))



#Lambda – Example/1
#Basic lambda:
from typing import Callable
square:Callable[[int], int] = lambda x: x ** 2
print(square(5)) # Output: 25
#This is functionally the same as:
def square(x:int) -> int:
    return x ** 2

#Lambda – Example/2
#Basic lambda:
from typing import Callable
multiply:Callable[[float, float], float] = lambda a, b: a * b
print(multiply(3, 4)) # Output: 12
#This is functionally the same as:
def square(a:float, b:float) -> float:
    return a * b


#Lambda – Example/3
#Basic lambda:
from typing import Callable
positive_or_negative:Callable[[int], str] = lambda x: "Positivo" if x > 0 else \
"Zero o Negativo"
print(positive_or_negative(5)) # Output: Positivo
print(positive_or_negative(-3)) # Output: Zero o Negativo
#This is functionally the same as:
def positive_or_negative(x:int) -> str:
    if x > 0:
        return "Positivo"
    else:
        return "Negativo"
    


#Lambda – Example/4
#Using with filter():
nums:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens:list[int] = list(filter(lambda x: x % 2 == 0, nums))
print(evens) # Output: [2, 4]

#Using with sorted():
names:list[str] = ['Alice', 'Bob', 'Charlie']
sorted_by_length = sorted(names, key=lambda name: len(name))
print(sorted_by_length) # Output: ['Bob', 'Alice', 'Charlie']


#Filtering strings using regex + lambda
import re
words:list[str] = ["abc123", "456", "hello", "98abc", "test999"]
# Keep only strings that contain only digits
only_digits = list(filter(lambda x: re.fullmatch(r"\d+", x), words))
print(only_digits) # Output: ['456’]

#Here:
#re.fullmatch(r"\d+", x): #checks if the entire string x is only digits.
#lambda: #defines this condition inline.
#filter(): applies lambda to every string in the list.



#Filtering strings using regex + lambda
import re
text:str = "Price: 100 dollars, Tax: 20 dollars"
# Multiply all numbers by 2 using a lambda
new_text = re.sub(r"\d+", lambda m: str(int(m.group()) * 2), text)
print(new_text) # Output: "Price: 200 dollars, Tax: 40 dollars"
#Here:
#re.sub(): replaces every number.
#lambda: dynamically computes the replacemen




