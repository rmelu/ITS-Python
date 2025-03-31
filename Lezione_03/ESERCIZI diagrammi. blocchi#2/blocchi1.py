max_posti = int(input("Inserisci il numero massimo dei posti: "))
liberi = max_posti
while True:
    opzione = input("Inserisci l'opzione (ingresso/uscita/stato/esci): ")
    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
            else:
                print("Non ci sono posti disponibili. ")
        case "uscita":
            if liberi < max_posti:
                liberi += 1
            else:
                print("Tutti posti sono già disponibili. ")
        case "stato":
            print(f"Posti liberi: {liberi}")
            print(f"Posti occupati: {max_posti - liberi} ")
        case "esci":
            break
        case _:
            print("Opzione non valida. ")
