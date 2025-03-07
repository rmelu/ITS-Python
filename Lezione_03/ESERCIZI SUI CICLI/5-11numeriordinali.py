#CREARE UNA LISTA DI NUMERI DA 1 A 9
numeri = list(range(1, 10))

#IRERA ATTRAVERSO LA LISTA DEI NUMERI
for numero in numeri:
    #DETERMINARE IL SUFFISSO ORDINALE IN BASE AL NUMERO
    if numero == 1:
        suffisso = "°"
    elif numero == 2:
        suffisso = "°"
    elif numero == 3:
        suffisso = "°"
    else:
        suffisso = "°"

    #STAMPA IL NUMERO ORDINALE
    print(f"{numero}{suffisso}")