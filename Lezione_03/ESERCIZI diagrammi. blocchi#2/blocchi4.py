n_tutor = 10
attesa = 0
while True:
    studente = int(input("Inserisci il numero di studenti che richiedono un tutor (o 0 per uscire): "))
    if studente == 0:
        break #esci dal ciclo
    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assegnato con successo. ")
    else:
        attesa += 1
        print("Studente in attesa! ")
    if attesa > 50:
        print("Troppi studenti in attesa. Assegnazione tutor sospesa. ")
        break
print(f"Tutor rimanenti: {n_tutor}")
print(f"Studenti in attesa: {attesa}")