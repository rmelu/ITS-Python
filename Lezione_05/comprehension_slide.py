'''#syntax:
#[expression for item in iterable if condition]
#Example:
# Traditional loop:
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)
#Comprehension:
squares = [x**2 for x in range(10) if x % 2 == 0]'''
'''

# Convert strings to uppercase
names:list[str] = ["alice", "bob", "carol"]
uppercase_names:list[str] = [name.upper() for name in names]
#Output -> ["ALICE", "BOB", "CAROL"]


# Flatten a list of lists
matrix:list[list[int]] = [[1, 2], [3, 4]]
flat:list[int] = [num for row in matrix for num in row]
#Output -> [1, 2, 3, 4]'''
'''

Syntax:
{expression for item in iterable if condition}
# Set comprehension
words = ["hi", "hello", "hey", "hi"]
unique_lengths = {len(word) for word in words}
Output -> {2, 3, 5}

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
Output -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
'''