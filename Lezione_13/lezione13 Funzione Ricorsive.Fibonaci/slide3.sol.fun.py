'''def countdown (n:int) -> None:
    #n is positive (n >= 0)
    if n >= 0:
        while n >=0:
        print(n)
        n = n -1
    else:
        print("errore il numero inserito è negativo ")
countdown(-5)        
countdown(-5)'''
    

def countdown (n:int) -> None:
    #n is positive (n >= 0)
    if n < 0:
        print("error")
    elif n == 0:
        print(0)
    else:
        print(n)
        countdown(n-1)

countdown(-5)
countdown(0)        
countdown(5)
    







'''def sum(n:int) -> None:
    if n < 0:
        print("errore")
        return None
    else:
        sum:int = 0
        while n >= 0:
            sum = sum + n
            n = n-1
        return int (sum)
print(sum(5))'''


'''def recursiveSum(n:int) -> int:
    if n < 0:
        print("error")
        return None
    elif n == 0:
        return 0
print(recursiveSum(5))'''

'''def rS(n:int) -> None:
    if n < 0:
        print("error")
        return None
    elif n == 0:
        return 0
    else:
        return int(n + rS(n-1))
print(rS(5))'''

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