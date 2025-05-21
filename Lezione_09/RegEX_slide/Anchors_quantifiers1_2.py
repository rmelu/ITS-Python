'''What is a Regular Expression?
A Regular Expression (RegEx) is a set of symbols (a string) used to identify a specific group of
strings, enabling the detection of patterns within a text.
Example use cases:
- finding emails;
- extracting numbers;
- identifying specific words'''
'''
Anchors ancore dizione l'inizio e fine linea
• ^ — Start-of-line anchor
Matches the position at the beginning of a string or line.
Example: ^Hello matches any line that starts with “Hello”.
• $ — End-of-line anchor
Matches the position at the end of a string or line.
Example: world$ matches any line that ends with “world”.
• ^Hello$
Matches the exact line “Hello” and nothing else.
'''

'''
Quantifiers/1  
• * — Zero or more
Matches 0 or more occurrences of the preceding element.
Example: abc* matches "ab", "abc", "abcc", "abccc", etc.
• + — One or more
Matches 1 or more occurrences of the preceding element.
Example: abc+ matches "abc", "abcc", "abccc", but not "ab".
• ? — Zero or one
Matches 0 or 1 occurrence of the preceding element.
Example: abc? matches "ab" or "abc".'''


'''Quantifiers/2
• {n} — Exactly n times
Examples: abc{3} matches "abccc" / a(bc){3} matches "abcbcbc"
• {n,} — At least n times
Example: abc{2,} matches "abcc", "abccc", "abcccc", etc.
• {n,m} — Between n and m times
Example: abc{2,4} matches "abcc", "abccc", or "abcccc".
'''