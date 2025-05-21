import re
text:str = "hello i have 10 year old, and i'm tall 178 longer -84"
numbers:list[str] = re.findall(r'-?\d+', text)
print(numbers)

#-?\d mi prende sia numeri negativi che positivi