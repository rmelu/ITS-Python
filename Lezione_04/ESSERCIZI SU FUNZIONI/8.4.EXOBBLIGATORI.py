def make_shirt(size="S", message="Amo Python"): # funzione con valori di default
    print(f"Taglia della maglietta: {size}")
    print(f"Messaggio sulla maglietta: {message}")
make_shirt()
make_shirt("M", "secondo tentativo!")
make_shirt("L","Programmo in python! ") # valori passati per posizione
make_shirt(size='XL', message="Fedeee") # valori passati per keyword