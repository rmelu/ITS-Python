stringa_originale = input("Inserisci una stringa: ")
stringa_invertita = ""

for i in range(len(stringa_originale) -1, -1, -1):
    stringa_invertita += stringa_originale[i]

print("La stringa invertita è:", stringa_invertita)
