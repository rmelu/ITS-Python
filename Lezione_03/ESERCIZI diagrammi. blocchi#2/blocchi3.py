max_posti = 100
while True:
    nome_corso = input("Inserisci il nome del corso (o 'esci' per terminare): ")
    if nome_corso.lower() == 'esci':
        break
    opzione = input("Iinserisci l'opzione (iscrivi/annula/visualizza/elimina): ")
    match opzione.lower():
        case 'iscrivi':
            if max_posti > 0:
                max_posti -= 1
                print(f"Iscrizione effetuata. Posti rimanenti: {max_posti}")
            else:
                print("Non ci sono posti disponibili. ")
        case 'annula':
            if max_posti < 100:
                max_posti += 1
                print(f"Annulamento effettuato. Posti rimanenti: {max_posti}")
            else:
                print("Tutti posti sono gia disponibili. ")
        case "visualizza":
            print(f"posti rimanenti: {max_posti}")
        case "elimina":
            max_posti = 100
            print("Tutti i posti sono stati liberati. ")
        case "esci":
            break
        case _:
            print("opzione non valida")


    

