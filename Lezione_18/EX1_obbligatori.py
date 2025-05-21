import math

def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return"Error: Cannot calculate the square root of a negative numbers."
    
print(safe_sqrt(9))
print(safe_sqrt(25))
print(safe_sqrt(-4))
print(safe_sqrt(0))
