numeri_pari = 0
numeri_dispari = []
conteggio_numeri = {}
while True:
    numero_str = input("Inserisci un numero (0 per terminare): ")
    if numero_str.replace(".", "", 1).isdigit():
        numero = float(numero_str)
        if numero.is_integer():
            numero = int(numero)
            if numero == 0:
                break
            if numero % 2 == 0:
                numeri_pari += numero
            else:
                numeri_dispari.append(numero)
            if numero in conteggio_numeri:
                conteggio_numeri[numero] += 1
            else:
                print("Input non valido. Inserisci un numero intero.")
        else:
             print("Input non valido. Inserisci un numero intero.")
if numeri_pari > 0:
    print(f"Somma dei numeri: {numeri_pari}")
else:
    print("Non sono stati inseriti numeri pari.")
if len(numeri_dispari) > 0:
    media_dispadi = sum(numeri_dispari) / len(numeri_dispari)
    print(f"Media dei numeri dispari : {media_dispadi}")
massima_frequenza = 0
numeri_piu_frequenti = []
for numero, frequenza in conteggio_numeri.items():
    if frequenza > massima_frequenza:
        massima_frequenza = frequenza
        numeri_piu_frequenti = [numero]
    elif frequenza == massima_frequenza:
        numeri_piu_frequenti.append(numero)
if len(numeri_piu_frequenti) > 0:
    if len(numeri_piu_frequenti) == 1:
        print(f"Numero più frequente: {numeri_piu_frequenti[0]} ({massima_frequenza} volte)")
    else:
        print("Numeri più frequenti:", end="")
        for i, numero in enumerate(numeri_piu_frequenti):
            print(f"{numero} ({massima_frequenza} volte)", end="")
            if i < len(numeri_piu_frequenti) -1:
                print(",", end=" ")
        print()
else:
    print("Non sono stati inseriti numeri")