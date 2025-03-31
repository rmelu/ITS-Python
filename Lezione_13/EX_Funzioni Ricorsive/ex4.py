def recursiveDigiCounter(n: int)-> int:
    n = abs(n)  #con la funzione abs possiamo inserire numeri negativi che succesivamente gli cambia in automatico in positivi
    if n < 10:
        return 1 
    else:
        return 1 + recursiveDigiCounter(n // 10)
    
print(recursiveDigiCounter(-120))
print(recursiveDigiCounter(3))
print(recursiveDigiCounter(50))