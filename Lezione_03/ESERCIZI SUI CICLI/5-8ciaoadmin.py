#ELENCO DI NOMI UTENTE
usernames = ["lia", "jon", "david", "leonard", "tomas"]

#CICLO ATTRAVERSO L'ELENCO DI NOMI UTENTE
for username in usernames:
    #VERIFICARE SÈ L'UTENTE È L'AMMINISTRATORE
    if username == "lia":
        print("Ciao lia, vuoi vedere un rapporto sullo stato?")
    else:
        print(f"Ciao {username}, grazie per aver effetuato di nuovo l'accesso. ")