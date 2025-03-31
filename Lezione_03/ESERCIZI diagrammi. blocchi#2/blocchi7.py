cont = 0
sum = 0

while True:
    scelta = input("Inserisci 'si' per inserire un voto o 'no' per calcolare la media: ")
    if scelta == 'si':
        voto = int(input("Inserisci il voto: "))
        if voto > 0:
            cont += 1
            sum += voto
        else:
            print("Errore: il voto deve essere positivo. ")
    elif scelta == 'no':
        if cont > 0:
            media = sum / cont
            print("La media voti è:", media)
        else:
            ("Nessun voto inserito. ")
        break  #interrompe il ciclo
    else:
        print("Scelta non valida. Inserisci 'si' o 'no'. ")