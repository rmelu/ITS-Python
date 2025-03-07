#sistema di prenotazione di posti
posti_totali = 20
posti_liberi = posti_totali
opzione = 0
while opzione !=4:     #Assumiamo che 4 sia l'opzione per uscire
    print("\n1. Prenota un posto")
    print("2. Aggiungi posti liberi")
    print("3. Visualizza posti liberi")
    print("4. Esci")

    opzione = int(input("Scegli un opzione: "))

    if opzione == 1: 
        if posti_liberi > 0:
            posti_liberi -= 1
            print("Posto prenotato con successo! ") 
        else:
            print("Non ci sono posti disponibili. ")
    elif opzione == 2:
        posti_liberi += int(input("Quanti posti vuoi aggiungere? "))
        if posti_liberi > posti_totali:
            print("Raggiunto il numero massimo di posti. ")
    elif opzione == 3:
        print("posti liberi:", posti_liberi)
    elif opzione == 4:
        print("Uscita dal sistema. ")
    else:
        print("Opzione non valida. ")
