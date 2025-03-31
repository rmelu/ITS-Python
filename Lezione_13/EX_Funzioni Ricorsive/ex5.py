def armonica(n: int) -> float:
    if n == 1:
        return 1.0
    else:
        return round((1 / n) * armonica(n - 1), 10)
    
print(armonica(6))  #in questo caso sarebbe (1 / 6) = 0,1666666667 poi faccio (6 - 1) = 5  poi il round di 10 dei risultati dati 
print(armonica(3))
print(armonica(1))
print(armonica(10))





