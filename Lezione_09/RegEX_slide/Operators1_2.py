
'''Operators/1
• | — Alternation (OR)
Matches either the expression before or after the operator.
Example: cat|dog matches "cat" or "dog".
• (…) — Grouping / Capture 
# esemio (abc){3} -> <<abcabcabc>> ['abc']va alla ricerca e va prendere l'ultimo valore che ha trovato!
Groups expressions together and captures matched text.
Captured groups can be reused or referenced later.
Example: (abc)+ matches "abc", "abcabc", etc.
• (?:...) — Non-capturing group
Groups expressions without capturing the matched text.
Useful for applying quantifiers or alternation without storing the result.
Example: (?:ab|cd)+ matches "ab", "cd", "abcd", etc'''


'''Operators/2
• (?=...) — Positive lookahead
Asserts that what follows the current position matches the expression.
Example: a(?=b) matches "a" only if it is followed by "b".
• (?!...) — Negative lookahead
Asserts that what follows does not match the expression.
Example: a(?!b) matches "a" only if it is not followed by "b".'''
'''

Boundary
• \b — Word boundary
Matches the position between a word character and a non-word character (or at
the start/end of a string next to a word character). Used to match whole words.
Example: \bcat\b matches "cat" within "the cat sat" but not "caterpillar“.
• \B — Non-word boundary
Matches a position that is NOT a word boundary. Useful for finding substrings inside
words.
Example: \Bcat\B matches "educate", but not "cat" or "catfish'''