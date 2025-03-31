########### R E P E A T ##########
 #LEGGI IL PRIMO VALORE
max_value = float(input("Inserisci il primo numero: "))
cont = 1
while True:
    n = float(input("Inserisci un numero: "))
    if n > max_value:    #CONTROLLARE SE È MAGGIORE
        max_value = n
    cont += 1          #INCREMENTARE CONTATORE
    if cont == 4:
        break
print("Il massimo valore è:", max_value)