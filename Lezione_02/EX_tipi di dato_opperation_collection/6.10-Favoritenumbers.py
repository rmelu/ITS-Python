numeri_preferiti = {
    "Rossi": [7,11,17],
    "Rosa": [8,3,10],
    "Roberto": [2,5,31]
}

for persona in numeri_preferiti:
    print(f"i numeri preferiti di{persona} sono:")    #(f) serve per inserire o formatare la stringa 
    for numero in numeri_preferiti[persona]:
        print(numero)
    print()

