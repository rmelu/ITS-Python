def sumInRange(a: int, b:int) -> None:
    if a > b:
        temp:int = a
        a = b
        b = temp
    sum:int = 0
    while b >= a:
        sum = sum + b
        #sum +=b
        b = b - 1
    return int(sum)

print(sumInRange(5,10))