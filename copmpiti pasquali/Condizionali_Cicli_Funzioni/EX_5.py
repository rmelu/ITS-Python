def integerPower(base:int, esponente:int) -> int:
    # base ^ 0 = 1
    if esponente == 0:
        return 1
    else:
        return int(base*integerPower(base, esponente - 1))
print(integerPower(3, 4))  #81
print(integerPower(4, 3))  #64
print(integerPower(2, 5))  #32
print(integerPower(5, 2))  #25



'''def recursivepower(base: int, esponente: int) -> int:
    if esponente == 0:
        return 1
    else:
        return base * recursivepower(base, esponente - 1)
    
risultato = recursivepower(3, 4)
print(risultato)'''