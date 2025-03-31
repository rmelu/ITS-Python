def recursiveSumInRange(a:int, b:int) -> int:
# if a > b, swap values of a and b
    if a > b:
# define a temporary variable called temp, containing value of a
        temp:int = a
# swap values of a and b
        a = b
        b = temp # now b = a
# if b = a, the recursive process must be stopped
    if b == a:
        return int(a)
    else:
        return int (b + recursiveSumInRange(a, b-1))
    
print(recursiveSumInRange(5, 10))
print(recursiveSumInRange(10, 5))