#conta i numeri pari e dispari
pari = 0
dispari = 0
cont = 0
while cont < 10:
    n = int(input("Inserisci un numero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
    cont += 1
print("Numeri pari:", pari)
print("Numeri dispari:", dispari)