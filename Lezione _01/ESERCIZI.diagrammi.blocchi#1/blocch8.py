#leggi la soglia dell'utente
soglia =int(input("Inserisci il valore della sogloia: "))

#interazione per 7 volte
for cont in range (7) :
    #leggi un numero dall'utente
    n = float(input("Inserisci numero: "))
    #controlla se il numero è maggiore della soglia
    if n > soglia:
            #se si, stampa numero
            print(f"numero maggiore della soglia: {n}")

 #fine del programma           
print("Fine del programma")

