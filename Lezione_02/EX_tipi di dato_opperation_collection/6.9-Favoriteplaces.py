#Creo il dizionario con i luoghi preferiti 
luoghi_preferiti = {
    "Cecile": ["Parigi", "Roma", "Londra"],
    "Marius": ["New York", "Tokio"],  
    "Gian marco": ["Barcellona", "Berlino", "Amsterdam"] 
}
#chiedo ai colleghi i loro luoghi preferiti
#Poi deconmmentare  queste righe e chiedere input reale
#nuovo_nome = input("inserisci un nome:")
#nuovi_luoghi = input("inserisci i suoi luoghi preferiti (separati da virgola): "). split (" ,")
#luoghi_preferiti[nuovo_nome] = nuovi_luoghi

#Stampo i risultati 

for persona in luoghi_preferiti:
    print("Luoghi preferitoi di", persona + ":")
    for luogo in luoghi_preferiti[persona]:
        print(" ~*~ "  +luogo)
    print() 








