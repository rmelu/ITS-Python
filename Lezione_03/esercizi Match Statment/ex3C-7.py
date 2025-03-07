countertesta = 0
countercroce = 0
print("Per ogni lancio della moneta inserisci \"t\" o\"T\" se è uscito \"testa\" mentre inserisci \"c\" o\"C\" se è uscito \"croce\".")
for i in range (1, 9):
    lancio = input(f"Lancio {i}: ").lower()
        
    match lancio:
        case 't':
            countertesta += 1
        case 'c' :
            countercroce += 1
        case _:
            print("valore non valido")

percentuale_testa = (countertesta / 8) * 100
percentuale_croce = (countercroce / 8) * 100

print(f"\n Totale \"testa\": {countertesta}")
print(f"percentuale \"testa\": {percentuale_testa:.2f}%")
print(f"\n Totale \"croce\": {countercroce}")
print(f"Percentuale \"croce\": {percentuale_croce:.2f}%")