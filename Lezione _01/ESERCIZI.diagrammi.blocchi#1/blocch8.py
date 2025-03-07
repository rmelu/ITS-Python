#leggi la soglia dell'utente
soglia =int(input("Inserisci il valore della sogloia: "))
#inizia il contatore
cont = 0
#inizia il ciclo while
while cont != 7:
    #leggi un numero dall'utente
    n = int(input("Inserisci numero: "))
    #controlla se il numero è maggiore della soglia
    if n > soglia:
            #se si, stampa numero
            print(n)
            #incrementa il contatore
            cont += 1
 #fine del programma           
print("Fine del programma")

