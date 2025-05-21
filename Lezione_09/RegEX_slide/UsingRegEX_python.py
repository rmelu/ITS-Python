#Using RegEx in Python

#Python includes the re module for regular expressions.
#Example:
import re
text:str = "My email is marco@gmail.com"
result:list[str] = re.findall(r'\S+@\S+', text)
print(result) # Output ['marco@gmail.com


#Using RegEx in Python
#Python includes the re module for regular expressions.
#Example:
import re
text:str = "My email is marco@gmail.com"
result:list[str] = re.findall(r'\S+@\S+', text)
print(result) # Output ['marco@gmail.com']



#Practical RegEx Examples/1
#Python includes the re module for regular expressions.
#Example:
#1. Starts with capital?
import re
text:str = "Rome"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group()) # Output "Rome"
#This regex means:
#• [A-Z]: Match one uppercase letter
#• [a-z]+: Match one or more lowercase letters
#So it matches a capitalized word.



#Practical RegEx Examples/2
#2. Find numbers:
import re
text:str = "I have 20 cats and 3 dogs"
numbers:list[str] = re.findall(r'\d+', text)
print(numbers) # Output ['2', '3']
#This regex means:
#• \d: matches a digit (0-9)
#• +: matches one or more consecutive digits
#So it matches all the integers found in the text



import re
text:str = "Il codice è: 123-ABC-abc"
match = re.search(r"(\d+)-([A-Z]+)-([a-z]+)", text)
if match:
    print("Intera corrispondenza:", match.group(0)) # Output: "123-ABC"
    print("Gruppo 1 (numeri):", match.group(1)) # Output: "123"
    print("Gruppo 2 (lettere):", match.group(2)) # Output: "ABC"
    print("Gruppo 3 (lettere):", match.group(3)) # Output: "abc"


#Substitution with Captured Groups
import re
text:str = "123-ABC"
new_text:str = re.sub(r"(\d+)-([A-Z]+)", r"\2-\1", text)
print(new_text) # Output: "ABC-123"


#Practical RegEx Non-Capturing Example
import re
text:str = "abcabcabc"
print("Cattura:", re.findall(r"(abc)+", text)) # Output ['abc']
print("Non cattura:", re.findall(r"(?:abc)+", text)) # Output ['abcabcabc’]


'''
Practical RegEx Non-Capturing Example
1. r"(abc)+" — Capturing Group
• This pattern uses a capturing group: (abc) means we’re grouping the string “abc”.
• The + applies to the entire group, so it will match one or more repetitions of "abc" — for example, "abcabcabc".
• However, when using re.findall() in Python, only the last match of the capturing group is returned.
• Even though the full match is "abcabcabc", findall() only gives back the content of the capturing group, and since the group
matched multiple times, only the last one (“abc”) is returned.
Result: ['abc']
2. r"(?:abc)+" — Non-Capturing Group
• Here, (?:abc) creates a non-capturing group — it groups “abc” for repetition, but does not save any individual part of the match.
• This tells Python: “Match the pattern, but don’t remember specific groups for extraction.”
• Now re.findall() returns the entire match, because there’s no capturing group to isolate.
• So "abcabcabc" is matched fully and returned as is.
Result: ['abcabcabc']'''