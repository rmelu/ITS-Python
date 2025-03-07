#ELENCO DI NOME UTENTES
usernames = []    #INIZIALMENTE VUOTO

#VERIFICARE SE L'ELENCO DEGLI UTENTI È VUOTO
if not usernames:
    print("Dobbiamo trovare alcuni utenti! ")
else:#CICLOATTRAVERSO L'ELENCO DEI NOMI UTENTE
    for username in usernames:
        #VERIFICARE SE L'UTENTE È L'AMMINISTRATORE
        if username == "admin":
            print("ciao admin, vuoi vedere un rapporto sullo stato? ")
        else:
            print(f"Ciao {username}, grazie per aver effetuato di nuovo l'accesso. ")
