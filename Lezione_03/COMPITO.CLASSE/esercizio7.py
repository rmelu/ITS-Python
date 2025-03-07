#Inizializzazione delle liste a e b 
n = int(input("Inserisci la lunghezza delle liste: ")) #chiediamo all'utente la lunghezza delle liste
a = []
b = []
for i in range(n):
    a.append(int(input(f"Inserisci l'elemento {i+1} della lista a: ")))
    b.append(int(input(f"Inserisci l'elemento {i+1} della lista b: ")))
#Calcolo della somma incrociata e memorizzazione nella lista c
c = []
for i in range(n):
    somma_incrociata = a[i] +b[n - 1 - i]    # Calcola la somma incrociata
    c.append(somma_incrociata)       #Aggiungi la somma alla lista c

#Visualizzazione delle liste 
print("Lista a:", a)
print("Lista b:", b)
print("Lista c (somma_incrociata):", c)