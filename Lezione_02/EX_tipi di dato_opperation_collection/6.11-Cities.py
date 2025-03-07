# Dizionario principale con le città come chiave

città = {
    "Parigi": { 
        "Paese": "Francia",
        "Popolazione": 2141000,    # abitanti circa
        "Fatto": "La Torre Eiffel è uno dei monumenti più visti al mondo."
    },
    "Londra": {
        "Paese": "Regno unito",
        "Popolazione": 9892000,  #abitanti circa
        "Fatto": "Il British Museum ospita una vasta collezione di arte e manufatti."  
    },
    "Roma": {
        "Paese": "Italia",
        "Popolazione": 2860000, #abitanti circa
        "Fatto": "Il Colosseo è un atinco anfiteatro Romano, simbolo della città."  
    }
} 
#Stampa delle informazioni su ogni città
for nome_città in città:
    print("informazioni su",nome_città + ':')
    print("Paese:", città[nome_città]["Paese"])
    print("Popolazione:", città[nome_città]["Popolazione"])
    print("Fatto:", città[nome_città]["Fatto"])
    print()  #Stampa una riga vuota per sapere la città  
    
    
    #la prox volta usa items!!!!!!!!!!!!!!!!!!!!!!!!!!!!

