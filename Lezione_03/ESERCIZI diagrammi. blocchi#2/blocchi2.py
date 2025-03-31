soglia = 70
#lettuta degli input
nord_sud = int(input("Inserisci il valore di nord_sud: "))
est_ovest = int(input("Inserisci il valore di est_ovest: "))

#controllo delle condizioni
if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40
elif est_ovest > soglia:
    time_ns = 40
    time_eo = 60
else:
    time_ns = (nord_sud/(nord_sud + est_ovest)) * 100
    time_eo = (est_ovest/ (nord_sud + est_ovest)) * 100
#stampa risultati
print("Il tempo assegnato alla direzione Nord_Sud è:", time_ns)
print("Il tempo assegnato alla direzione Est_ovest è:", time_eo)