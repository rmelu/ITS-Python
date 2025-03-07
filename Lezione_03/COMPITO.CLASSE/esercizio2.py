stringa = input("Inserisci una stringa: ")
numero_spazi = 0
for carattere in stringa:
    if carattere == " ":
        numero_spazi +=1
print("Il numero di spazi nella stringa è:", numero_spazi)      