'''def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    Somma = 0
    for numero in numbers:
        if numero > threshold:
            Somma += numero
            return Somma
print(sum_above_threshold([2, 5, 1], 1))'''

def is_magic_number(num: int) -> bool:
    num_str = str(num)
    if '7' in num_str:
        return True
    else:
        return False
    
print(is_magic_number(123))