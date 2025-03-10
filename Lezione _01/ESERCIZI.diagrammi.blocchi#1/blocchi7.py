#conta i numeri pari e dispari
pari = 0
dispari = 0

for cont in range(10):
    n = int(input("Inserisci un numero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
        
print("Numeri pari:", pari)
print("Numeri dispari:", dispari)