n_euro = int(input("Inserisci il numero di euro dsponibili: "))

barrette_totali = 0
buoni_totali = 0

#Aquisto iniziale con gli euro disponibili
barrete_aquistate = n_euro
barrette_totali += barrete_aquistate
buoni_totali += barrete_aquistate

#Ciclo di scambio buoni
while buoni_totali >= 6:
    barrete_gratuite = buoni_totali // 6    #Divizione intera per ottenere il numero di barrete gratuite
    barrette_totali += barrete_gratuite
    buoni_totali -= barrete_gratuite *6     #Sotraggo i buoni usati
    buoni_totali += barrete_gratuite        # Aggiungo i buoni delle barrette gratuite
print("Numero totali di barrette ottenute:", barrette_totali)
print("Buoni sconto avanzati :", buoni_totali)