while True:
    parola = input("Inserisci una parola (o 'fine per terminare): ")
        
    match parola:
        case "fine":
            break #Esci dal ciclo se viene inserita la parola "fine"
        case parola if len(parola) > 0 and parola[0] == parola[-1]:
            print(f"La parola '{parola}' inizia e finisce con lo stesso carattere.")
        case _:
            print(f"La parola '{parola}' non inzia e finisce con lo stesso carattere.")