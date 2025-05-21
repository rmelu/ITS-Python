'''Character class/1

• […] — Character class
Matches any single character of the characters inside the brackets.
Example: gr[ae]y matches "gray" or "grey".
Ranges:
• [a-z]
Matches any lowercase letter from a to z.
• [0-9]
Matches any digit from 0 to 9.'''


'''Character class/2

Negation:
• [^abc]
Matches any character except a, b, or c.
The ^ inside brackets means “not”.
Combining Classes:
• [a-zA-Z0-9_]
Matches any letter, digit, or underscore.'''
'''

Character class/3
• \d — Digit
Matches any single digit (equivalent to [0-9])
Example: \d\d matches "42", "99"
• \D — Non-digit
Matches any character that is NOT a digit (equivalent to [^0-9])
Example: \D+ matches "abc"'''

'''
Character class/4
• \w — Word character
Matches any letter, digit, or underscore (equivalent to [a-zA-Z0-9_])
Example: \w+ matches "hello123", "my_variable"
• \W — Non-word character
Matches any character that is NOT a word character (equivalent to [^a-zA-Z0-9_])
Example: \W+ matches spaces, punctuation, symbols like "!", "#", " ".'''

'''
Character class/5
• \s — Whitespace character
Matches any space, tab, newline, etc.
Example: \s+ matches " " or "\n\t"
• \S — Non-whitespace character
Matches any character that is NOT a space, tab, or newline
Example: \S+ matches words and symbols, skipping whitespace.'''