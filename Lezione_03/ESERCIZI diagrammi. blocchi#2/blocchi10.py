eta = int(input("Inserisci l'eta: "))

if eta >= 18 and eta <= 65:
    print("Puoi partecipare all'attivita")
else:
    if eta < 18:
        print("Non puoi partecipare all'attivita perchè non hai raggiunto l'età minima richiesta. ")
    else:
        print("Non puoi partecipare all'attività perchè hai superto l'età massima consentita. ")