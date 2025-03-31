def Pi3_fattori(n: int) -> int:
    risultato = 1
    for i in  range(1, n + 1):
        risultato  *= i**3
    return risultato

print(Pi3_fattori(5))
print(Pi3_fattori(2))
print(Pi3_fattori(10))
    