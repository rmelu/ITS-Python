#ELENCO DI NOMI UTENTE ESISTENTI
current_users = ["lia", "tomas", "david", "leonard"]

#ELENCO DI NUOVI NOMI UTENTE
new_users = ["frank", "grece", "john", "alice"]

#Creo una coppia di current_user con i nomi utente in minuscolo
current_user_lower = [user.lower() for user in current_users]

#CICLO ATTRAVERSO L'ELENCO DI NUOVI NOMI UTENTE
for new_user in new_users:
    #VERIFICARE SE IL NIUOVO NOME UTENTYE (IN MINUSCOLO) È GIA IN USO
    if new_user.lower() in current_user_lower:
        print(f"Il nome utente '{new_user}' non è disponibile. Inserisci un nuovo nome utente.")
    else:
        print(f"Il nome utente '{new_user}' è disponibile. ")