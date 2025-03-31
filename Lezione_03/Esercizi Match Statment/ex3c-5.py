utente = {}
utente["nome"] = input("Digitare nome dell'utente: ")
utente["ruolo"] =input ("Digitare il ruolo dell'utente: ")
utente["eta"] = input("Digitare l'eta dell'utente: ")

match utente["ruolo"]:
    case "admin": 
        print("Accesso completo a tutte le funzionalità")
    case "moderatore":
        print(f" Salve {utente['nome']}! può gestire i contenuti ma non modificare le impostazioni.")
    case "utente":
        if utente["età"] >= 18:
            print("Accesso standard a tutti i servizi") 
        else:
            print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case "ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti!")
    case _:
        print("Attenzione Ruolo non riconosciuto! Accesso Negato")