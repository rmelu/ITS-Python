n1 = int(input("Inserisci il primo numero intero (n1): "))
n2 = int(input("Inserisci il secondo numero intero (n2): "))
prodotto = 1   # Inizializza il prodotto a 1 (neutro per la moltiplicazione)

if n1 <= n2:    #Gestisce il caso n1 <= n2
    for i in range(n1, n2 + 1):    #Intera da n1 a n2 (inclusi)
        prodotto *= i
else:            #Gestisce il caso n1 > n2
    for i in range(n2, n1 + 1):       #Intera da n2 a n1 (inclusi)
        prodotto *= i
print("Il prodotto dei numeri compresio tra", n1, "e", n2, "e", prodotto)