#INIZIALIZZAZIONE DELLE VARIABILI
sum_value = 0
cont = 0
# Ciclo per 5  iterazioni
while True:
    n = float(input("Inserisci un numero: "))     #Leggi il numero
    if n > 0:    #Se il nnumero è positivo, lo aggiunge alla somma 
        sum_value += n
    cont += 1   # Incrementa il contattore 
    if cont == 5:
        break
    #Stampa il risultato
print("La somma dei numeri positivi è:", sum_value)
              